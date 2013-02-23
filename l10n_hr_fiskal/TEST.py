# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Module: l10n_hr_fiskal
#    Author: Davor Bojkić
#    mail:   bole@dajmi5.com
#    Copyright (C) 2012- Daj Mi 5, 
#                  http://www.dajmi5.com
#    Contributions: Hrvoje ThePython - Free Code!
#                   Goran Kliska (AT) Slobodni Programi
#                    
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields,osv



class test_table(osv.Model):
    _name = 'testtable'
    _description ='Testing purposes table - to be removed'
    
    def dummy(self):
        pass   
    
    def _neka_suma(self,cr,uid,ids,field,arg,context=None):
        tra=self.read(cr, uid, fields, context=None)
        res=tra.br1 + tra.br2
        return {'suma':res
                }



    def promjena1(self,cr,uid,ids,br1,br2,context=None):
        a=br1+br2
        b=str(br1)+str(br2)
        return{'br2':a,
               'test1':b}
        
        
    _columns={
              'name':fields.char('name', size=25),
              'br1':fields.integer('BR1'),
              'br2':fields.integer('BR2'),
              'test1':fields.char('test1',size=25),
              'test2':fields.char('test2',size=125),
              'dane':fields.boolean('DaNe'),
              #'suma':fields.function(_neka_suma,string='test sume',type='integer')
              }