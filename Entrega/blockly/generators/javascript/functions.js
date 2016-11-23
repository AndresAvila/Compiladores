'use strict';

goog.provide('Blockly.JavaScript.functions');
goog.require('Blockly.JavaScript');



//

Blockly.JavaScript['function'] = function(block) {
  var dropdown_name = block.getFieldValue('NAME');
  var text_nombrefuncion = block.getFieldValue('nombreFuncion');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_bloquefuncion = Blockly.JavaScript.statementToCode(block, 'bloqueFuncion');
  var code = 'function ' + dropdown_name + ' ' + text_nombrefuncion  + value_name  + ' {\n' + statements_bloquefuncion + '}';
  return code;
};

Blockly.JavaScript['unparametro'] = function(block) {
  var dropdown_name = block.getFieldValue('NAME');
  var text_nombreparam = block.getFieldValue('nombreParam');
  // TODO: Assemble JavaScript into code variable.
  var code =  dropdown_name + ' ' + text_nombreparam; 
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['masparam'] = function(block) {
  var dropdown_name = block.getFieldValue('NAME');
  var text_nombreparam = block.getFieldValue('nombreParam');
  var value_masparametros = Blockly.JavaScript.valueToCode(block, 'masParametros', Blockly.JavaScript.ORDER_ATOMIC);
  value_masparametros = value_masparametros.substring(1,value_masparametros.length - 1);
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_name + ' ' + text_nombreparam + ', ' + value_masparametros;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['llamada'] = function(block) {
  var text_nombrefunc = block.getFieldValue('nombreFuncLlamada');
  var value_call = Blockly.JavaScript.valueToCode(block, 'callFunc', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'call: ' + text_nombrefunc + value_call;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['return'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  value_name = value_name.substring(1, value_name.length - 1);
  
  var code = 'return ' + value_name +';\n';
  return code;
};