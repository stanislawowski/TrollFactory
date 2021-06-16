#!/usr/bin/env python3
# -*- coding: utf8 -*-
from fpdf import FPDF

def fix_title(s):
    return s.replace('_', ' ').capitalize()

def generate_pdf(personality, id):
    pdf = FPDF(format='A4')
    pdf.add_page()
    pdf.add_font('PTSans', '', 'static/fonts/PTSans-Regular.ttf', uni=True)
    pdf.add_font('PTSans', 'B', 'static/fonts/PTSans-Bold.ttf', uni=True)

    pdf.image('static/img/pdf_header.png', 0, 0, 210)
    pdf.set_font('PTSans', 'B', 12)
    pdf.cell(60, 25, 'https://trollfactory.tk/' + str(id), 0, 1, '')
    
    for i in range(30):
        pdf.image('static/img/dna_strand.png', 180, 0+i*31.8, 13)

    for prop_name in personality.keys():
        pdf.set_font('PTSans', 'B', 12)
        pdf.cell(60, 6, personality[prop_name]['prop_title'], 0, 1, 'C')

        pdf.set_font('PTSans', '', 12)
        for prop_entry in personality[prop_name].keys():
            if prop_entry == 'user_agent':
                for part in personality[prop_name][prop_entry]:
                    pdf.cell(0, 6, str(part), 0, 1)
            elif prop_entry != 'prop_title':
                line = fix_title(prop_entry)+': '+str(personality[prop_name][prop_entry])
                pdf.cell(0, 6, line, 0, 1)

        pdf.ln(4)
    
    pdf.output(''.join(['personalities/', str(id), '.pdf']), 'F')
