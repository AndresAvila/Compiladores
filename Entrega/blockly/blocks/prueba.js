'use strict';

goog.provide('Blockly.Blocks.prueba');
goog.require('Blockly.Blocks');
Blockly.Blocks['prueba'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("var:");
    this.setColour(20);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};