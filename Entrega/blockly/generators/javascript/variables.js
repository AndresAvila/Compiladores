'use strict';
goog.provide('Blockly.JavaScript.variables');
goog.require('Blockly.JavaScript');





//

Blockly.JavaScript['assignment'] = function(block) {
  var text_name = block.getFieldValue('NAME');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(!value_name) {
    value_name = '0';
  }
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = text_name + ' = ' + value_name + ';\n';
  return code;
};

Blockly.JavaScript['assignment_arr'] = function(block) {
  var text_name = block.getFieldValue('NAME');
  var text_exp = block.getFieldValue('EXP');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var code = text_name + ' [ ' + text_exp + ' ] = ' + value_name + ';\n';
  return code;
};

Blockly.JavaScript['var'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var code = text_var;
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['var_coma'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  value_name = value_name.substring(1,value_name.length-1);
  var code = text_var + ', ' + value_name;
  return [code, Blockly.JavaScript.ORDER_NONE];
};




  Blockly.JavaScript['decvariables'] = function(block) {
  var value_varname = Blockly.JavaScript.valueToCode(block, 'varName', Blockly.JavaScript.ORDER_ATOMIC);
  var dropdown_type = block.getFieldValue('type');
  value_varname = value_varname.substring(1, value_varname.length-1);
  // TODO: Assemble JavaScript into code variable.
  var code = 'var ' + value_varname + ' : ' + dropdown_type + ';\n';
  return code;

};


Blockly.JavaScript['decarreglos'] = function(block) {
  var text_varnombre = block.getFieldValue('varNombre');
  var dropdown_name = block.getFieldValue('NAME');
  var text_tam = block.getFieldValue('tam');
  // TODO: Assemble JavaScript into code variable.
  var code = 'var ' + text_varnombre + ' : ' + dropdown_name + ' [' + text_tam + '];\n'   ;
  return code;
};

Blockly.JavaScript['asigarr'] = function(block) {
  var text_nomarr = block.getFieldValue('nomArr');
  var text_tamarr = block.getFieldValue('tamArr');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  value_name = value_name.substring(1,value_name.length-1);
  // TODO: Assemble JavaScript into code variable.
  var code = text_nomarr + ' [' + text_tamarr + '] = '  + value_name + ';\n';
  return code;
};