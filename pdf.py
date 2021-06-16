from fpdf import FPDF

def fix_enc(s):
    return s.encode('latin-1', 'ignore').decode('latin-1')

def fix_title(s):
    return s.replace('_', ' ').capitalize()

def generate_pdf(personality, id):
    pdf = FPDF(format='A4')
    pdf.add_page()
    
    for prop_name in personality.keys():
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(60, 10, personality[prop_name]['prop_title'], 0, 1, 'C')

        pdf.set_font('Arial', '', 16)
        for prop_entry in personality[prop_name].keys():
            if prop_entry == 'user_agent':
                for part in personality[prop_name][prop_entry]:
                    pdf.cell(0, 10, fix_enc(str(part)), 0, 1)
            elif prop_entry != 'prop_title':
                line = fix_enc(fix_title(prop_entry)+': '+str(personality[prop_name][prop_entry]))
                pdf.cell(0, 10, line, 0, 1)

        pdf.ln(5)
    
    pdf.output(''.join(['personalities/', str(id), '.pdf']), 'F')
