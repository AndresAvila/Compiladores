'use strict';

goog.provide('Blockly.Blocks.texts');
goog.require('Blockly.Blocks');

Blockly.Blocks.texts.HUE = 160;



Blockly.Blocks['char_var'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("'")
        .appendField(new Blockly.FieldTextInput("a"), "VAR")
        .appendField("'");
    this.setOutput(true);
    this.setColour(160);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['char_var_dos'] = {
  init: function() {
    this.appendValueInput("Valor")
        .appendField("'")
        .appendField(new Blockly.FieldTextInput("a"), "VAR")
        .appendField("'");
    this.setOutput(true);
    this.setColour(160);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['print'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("print");

    this.appendValueInput("args");
    
    this.setInputsInline(true);
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(160);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};