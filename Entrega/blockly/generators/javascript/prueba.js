'use strict';
goog.provide('Blockly.JavaScript.prueba');
goog.require('Blockly.JavaScript');

Blockly.JavaScript['prueba'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '...;\n';
  return code;
};

