# Generated from grammar/covid19.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .covid19Parser import covid19Parser
else:
    from covid19Parser import covid19Parser

from semantics import *


# This class defines a complete listener for a parse tree produced by covid19Parser.
class covid19Listener(ParseTreeListener):

    # Enter a parse tree produced by covid19Parser#nocondicional.
    def enterNocondicional(self, ctx:covid19Parser.NocondicionalContext):
        pass

    # Exit a parse tree produced by covid19Parser#nocondicional.
    def exitNocondicional(self, ctx:covid19Parser.NocondicionalContext):
        pass


    # Enter a parse tree produced by covid19Parser#condicional.
    def enterCondicional(self, ctx:covid19Parser.CondicionalContext):
        pass

    # Exit a parse tree produced by covid19Parser#condicional.
    def exitCondicional(self, ctx:covid19Parser.CondicionalContext):
        pass


    # Enter a parse tree produced by covid19Parser#bloque.
    def enterBloque(self, ctx:covid19Parser.BloqueContext):
        pass

    # Exit a parse tree produced by covid19Parser#bloque.
    def exitBloque(self, ctx:covid19Parser.BloqueContext):
        pass


    # Enter a parse tree produced by covid19Parser#decision.
    def enterDecision(self, ctx:covid19Parser.DecisionContext):
        pass

    # Exit a parse tree produced by covid19Parser#decision.
    def exitDecision(self, ctx:covid19Parser.DecisionContext):
        pass


    # Enter a parse tree produced by covid19Parser#cargadatos.
    def enterCargadatos(self, ctx:covid19Parser.CargadatosContext):
        pass

    # Exit a parse tree produced by covid19Parser#cargadatos.
    def exitCargadatos(self, ctx:covid19Parser.CargadatosContext):
        pass


    # Enter a parse tree produced by covid19Parser#cte.
    def enterCte(self, ctx:covid19Parser.CteContext):
        pass

    # Exit a parse tree produced by covid19Parser#cte.
    def exitCte(self, ctx:covid19Parser.CteContext):
        pass


    # Enter a parse tree produced by covid19Parser#lectura.
    def enterLectura(self, ctx:covid19Parser.LecturaContext):
        pass

    # Exit a parse tree produced by covid19Parser#lectura.
    def exitLectura(self, ctx:covid19Parser.LecturaContext):
        pass


    # Enter a parse tree produced by covid19Parser#escritura.
    def enterEscritura(self, ctx:covid19Parser.EscrituraContext):
        pass

    # Exit a parse tree produced by covid19Parser#escritura.
    def exitEscritura(self, ctx:covid19Parser.EscrituraContext):
        pass


    # Enter a parse tree produced by covid19Parser#megaexpresion.
    def enterMegaexpresion(self, ctx:covid19Parser.MegaexpresionContext):
        pass

    # Exit a parse tree produced by covid19Parser#megaexpresion.
    def exitMegaexpresion(self, ctx:covid19Parser.MegaexpresionContext):
        pass


    # Enter a parse tree produced by covid19Parser#superexpresion.
    def enterSuperexpresion(self, ctx:covid19Parser.SuperexpresionContext):
        pass

    # Exit a parse tree produced by covid19Parser#superexpresion.
    def exitSuperexpresion(self, ctx:covid19Parser.SuperexpresionContext):
        pass


    # Enter a parse tree produced by covid19Parser#expresion.
    def enterExpresion(self, ctx:covid19Parser.ExpresionContext):
        pass

    # Exit a parse tree produced by covid19Parser#expresion.
    def exitExpresion(self, ctx:covid19Parser.ExpresionContext):
        pass


    # Enter a parse tree produced by covid19Parser#termino.
    def enterTermino(self, ctx:covid19Parser.TerminoContext):
        pass

    # Exit a parse tree produced by covid19Parser#termino.
    def exitTermino(self, ctx:covid19Parser.TerminoContext):
        pass


    # Enter a parse tree produced by covid19Parser#factor.
    def enterFactor(self, ctx:covid19Parser.FactorContext):
        pass

    # Exit a parse tree produced by covid19Parser#factor.
    def exitFactor(self, ctx:covid19Parser.FactorContext):
        pass


    # Enter a parse tree produced by covid19Parser#estatuto.
    def enterEstatuto(self, ctx:covid19Parser.EstatutoContext):
        pass

    # Exit a parse tree produced by covid19Parser#estatuto.
    def exitEstatuto(self, ctx:covid19Parser.EstatutoContext):
        pass


    # Enter a parse tree produced by covid19Parser#llamadametodo.
    def enterLlamadametodo(self, ctx:covid19Parser.LlamadametodoContext):
        pass

    # Exit a parse tree produced by covid19Parser#llamadametodo.
    def exitLlamadametodo(self, ctx:covid19Parser.LlamadametodoContext):
        pass


    # Enter a parse tree produced by covid19Parser#regresa.
    def enterRegresa(self, ctx:covid19Parser.RegresaContext):
        pass

    # Exit a parse tree produced by covid19Parser#regresa.
    def exitRegresa(self, ctx:covid19Parser.RegresaContext):
        pass


    # Enter a parse tree produced by covid19Parser#asignacion.
    def enterAsignacion(self, ctx:covid19Parser.AsignacionContext):
        pass

    # Exit a parse tree produced by covid19Parser#asignacion.
    def exitAsignacion(self, ctx:covid19Parser.AsignacionContext):
        pass


    # Enter a parse tree produced by covid19Parser#identificador_accesa.
    def enterIdentificador_accesa(self, ctx:covid19Parser.Identificador_accesaContext):
        pass

    # Exit a parse tree produced by covid19Parser#identificador_accesa.
    def exitIdentificador_accesa(self, ctx:covid19Parser.Identificador_accesaContext):
        pass


    # Enter a parse tree produced by covid19Parser#identificador_definicion.
    def enterIdentificador_definicion(self, ctx:covid19Parser.Identificador_definicionContext):
        pass

    # Exit a parse tree produced by covid19Parser#identificador_definicion.
    def exitIdentificador_definicion(self, ctx:covid19Parser.Identificador_definicionContext):
        pass


    # Enter a parse tree produced by covid19Parser#programa.
    def enterPrograma(self, ctx:covid19Parser.ProgramaContext):
        pass

    # Exit a parse tree produced by covid19Parser#programa.
    def exitPrograma(self, ctx:covid19Parser.ProgramaContext):
        pass


    # Enter a parse tree produced by covid19Parser#varx.
    def enterVarx(self, ctx:covid19Parser.VarxContext):
        pass

    # Exit a parse tree produced by covid19Parser#varx.
    def exitVarx(self, ctx:covid19Parser.VarxContext):
        pass


    # Enter a parse tree produced by covid19Parser#var.
    def enterVar(self, ctx:covid19Parser.VarContext):
        pass

    # Exit a parse tree produced by covid19Parser#var.
    def exitVar(self, ctx:covid19Parser.VarContext):
        pass


    # Enter a parse tree produced by covid19Parser#funcp.
    def enterFuncp(self, ctx:covid19Parser.FuncpContext):
        pass

    # Exit a parse tree produced by covid19Parser#funcp.
    def exitFuncp(self, ctx:covid19Parser.FuncpContext):
        pass


    # Enter a parse tree produced by covid19Parser#tipo.
    def enterTipo(self, ctx:covid19Parser.TipoContext):
        pass

    # Exit a parse tree produced by covid19Parser#tipo.
    def exitTipo(self, ctx:covid19Parser.TipoContext):
        pass


    # Enter a parse tree produced by covid19Parser#metodo.
    def enterMetodo(self, ctx:covid19Parser.MetodoContext):
        pass

    # Exit a parse tree produced by covid19Parser#metodo.
    def exitMetodo(self, ctx:covid19Parser.MetodoContext):
        pass



del covid19Parser