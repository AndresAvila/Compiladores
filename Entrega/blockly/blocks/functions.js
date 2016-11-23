'use strict';

goog.provide('Blockly.Blocks.functions');
goog.require('Blockly.Blocks');



//

Blockly.Blocks['function'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("function")
        .appendField(new Blockly.FieldDropdown([["int", "int"], ["float", "float"], ["string", "string"], ["bool", "bool"], ["char", "char"]]), "NAME")
        .appendField(new Blockly.FieldTextInput(""), "nombreFuncion");
         
    this.appendStatementInput("bloqueFuncion")
        .setCheck(null);
        
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(65);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['unparametro'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["int", "int"], ["float", "float"], ["string", "string"], ["bool", "bool"], ["char", "char"]]), "NAME")
        .appendField(new Blockly.FieldTextInput(""), "nombreParam");
    this.setOutput(true, null);
    this.setColour(65);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['masparam'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["int", "int"], ["float", "float"], ["string", "string"], ["bool", "bool"], ["char", "char"]]), "NAME")
        .appendField(new Blockly.FieldTextInput(""), "nombreParam");
    this.appendValueInput("masParametros")
        .setCheck(null);
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setColour(65);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['return'] = {
  init: function() {
    this.appendValueInput("NAME")
        .appendField("return");
    this.setPreviousStatement(true);
    this.setColour(65);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['llamada'] = {
  init: function() {
    this.appendValueInput("callFunc")
        .setCheck(null)
        .appendField("call:")
        .appendField(new Blockly.FieldTextInput(""), "nombreFuncLlamada");
    this.setOutput(true, null);
    this.setColour(65);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

