'use strict';

goog.provide('Blockly.JavaScript.texts');
goog.require('Blockly.JavaScript');



Blockly.JavaScript['char_var'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var code = '\'' + text_var + '\'';
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['char_var_dos'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'Valor', Blockly.JavaScript.ORDER_ATOMIC);
  value_name = value_name.substring(1,value_name.length-1);
  var code = '\'' + text_var  + '\'' + ', ' + value_name;
  return [code, Blockly.JavaScript.ORDER_NONE];
};


Blockly.JavaScript['print'] = function(block) {
  var value_args = Blockly.JavaScript.valueToCode(block, 'args', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'print ' + value_args + ';\n';
  return code;
};