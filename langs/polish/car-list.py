import requests, json 

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def main ():
	r = requests.get("https://otomoto.pl")

	try:
		data = json.loads(find_between(find_between(r.text, '<script id="__NEXT_DATA__" type="application/json"', 'cript>'), '==">', '</s'))
	except:
		print('[!] failed to parse/find data!')
		return 

	data = data['props']['pageProps']

	totalProducts = 0

	carBrandsOriginal = data['filters']['571']['_meta']['values'][1]['group_values']
	carBrandsTransformed = []
	
	for carBrand in carBrandsOriginal: 
		carBrandTransformed = {}
		carBrandTransformed['value_key'] = carBrand['value_key']

		carBrandTransformed['name'] = carBrand['name'].split(' (')[0]
		carBrandTransformed['products'] = int(carBrand['name'].split(' (')[1][:-1])

		if (carBrandTransformed['products'] == 0):
			continue

		totalProducts += carBrandTransformed['products']

		carBrandsTransformed.append(carBrandTransformed)

	# lets calculate the brands weights now
	for carBrandKey, carBrand in enumerate(carBrandsTransformed):
		carBrandsTransformed[carBrandKey]['weight'] = ((carBrand['products'] / totalProducts) * 100)

	# we have all brand's keys which we need to get models for each brand, so lets do it

	carModels = [] # key: brand name, value: car model 

	for carBrand in carBrandsTransformed:
		carModelsTemp = []
		
		brandModels = data['filtersValues']['573:571:' + carBrand['value_key']][0]['group_values'] 
		for brandModel in brandModels:
			carModel = {}

			carModel['name'] = brandModel['name'].split(' (')[0]
			carModel['products'] = int(brandModel['name'].rsplit(' (', 1)[1][:-1])

			if (carModel['products'] == 0):
				continue

			carModel['weight'] = ((carModel['products'] / totalProducts) * 100) 

			if '3018:573:' + brandModel['value_key'] in data['filtersValues']:
				generations = [] 
				for generation in data['filtersValues']['3018:573:' + brandModel['value_key']][0]['group_values']:
					generationName = generation['name'].split(' (')[0]
					generationProducts = int(generation['name'].rsplit(' (', 1)[1][:-1])

					if (generationProducts == 0):
						continue 

					generations.append({
						'generation_name': generationName,
						'generation_weight': ((generationProducts / totalProducts) * 100)
					})

				carModel['generations'] = generations

			carModelsTemp.append(carModel)

		carModels.append({
			"brand_name": carBrand['name'],
			"brand_weight": carBrand['weight'],
			"models": carModelsTemp
		})

	with open('car-list.json', 'w', encoding='utf-8') as f:
		json.dump(carModels, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
	main()