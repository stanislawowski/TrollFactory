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
    
    for prop_name in personality.keys():
        pdf.set_font('PTSans', 'B', 16)
        pdf.cell(60, 10, personality[prop_name]['prop_title'], 0, 1, 'C')

        pdf.set_font('PTSans', '', 16)
        for prop_entry in personality[prop_name].keys():
            if prop_entry == 'user_agent':
                for part in personality[prop_name][prop_entry]:
                    pdf.cell(0, 10, str(part), 0, 1)
            elif prop_entry != 'prop_title':
                line = fix_title(prop_entry)+': '+str(personality[prop_name][prop_entry])
                pdf.cell(0, 10, line, 0, 1)

        pdf.ln(5)
    
    pdf.output(''.join(['personalities/', str(id), '.pdf']), 'F')
