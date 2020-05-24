SHOW_VIRTUAL = False

from grammar.covid19SemanticCube import semanticCube
from virtualmemory import MemorySegment

class Quad:
  def __init__(self, operator, operand_left, operand_right, result_id):
    self.operator = operator
    self.operand_left = operand_left
    self.operand_right = operand_right
    self.result_id = result_id

  def __repr__(self):
    return "Quad({}, {}, {}, {})".format(
      self.operator,
      self.operand_left,
      self.operand_right,
      self.result_id,
    )

class VarCount:
  def __init__(self, int_type=0, float_type=0, char_type=0, string_type=0, dataframe_type=0):
    self.int_type = int_type
    self.float_type = float_type
    self.char_type = char_type
    self.string_type = string_type
    self.dataframe_type = dataframe_type
  
  def increment(self, var_type):
    if(var_type == "string"):
      self.string_type += 1
    elif(var_type == "int"):
      self.int_type += 1
    elif(var_type == "float"):
      self.float_type += 1
    elif(var_type == "char"):
      self.char_type += 1
    elif(var_type == "Dataframe"):
      self.dataframe_type += 1
  
  def __add__(self, var_counter): 
      string_type = self.string_type + var_counter.string_type
      int_type = self.int_type + var_counter.int_type
      float_type = self.float_type + var_counter.float_type
      char_type = self.char_type + var_counter.char_type
      dataframe_type = self.dataframe_type + var_counter.dataframe_type
      return VarCount(int_type, float_type, char_type, string_type, dataframe_type)

  def __repr__(self):
    return "VarCount({}, {}, {}, {}, {})".format(
      self.int_type,
      self.float_type,
      self.char_type,
      self.string_type,
      self.dataframe_type,
    )
    
class Variable:
  def __init__(self, name, type, dimensions, memory_cell):
    self.name = name
    self.type = type
    self.dimensions = dimensions
    self.memory_cell = memory_cell

  def __repr__(self):
    return "Variable({}, {}, {})".format(self.name, self.type, self.dimensions)

class Constant:
  def __init__(self, value, type, memory_cell):
    self.value = value
    self.type = type
    self.memory_cell = memory_cell
  def __repr__(self):
    return "CTE({} : {})".format(self.type, self.value)

class Function:
  def __init__(self, name, var_type, params, first_quad, var_count, vars_table):
    self.name = name
    self.type = var_type
    self.params = params
    self.first_quad = first_quad
    self.var_count = var_count
    self.vars_table = vars_table

  def __repr__(self):
    return "Function({}, {}, {}, {}, {}, {})".format(self.name, self.type, str(self.params), self.first_quad, self.size, str(self.vars_table))

virtual_memory = {
    'global': {
        'int': MemorySegment(0, 1800, 0),
        'float': MemorySegment(1800, 1800, 0),
        'char': MemorySegment(3600, 600, 0),
        'string': MemorySegment(4200, 600, 0),
        'Dataframe': MemorySegment(4800, 1200, 0),
    },
    'temporary': {
        'int': MemorySegment(6000, 3000, 0),
        'float': MemorySegment(9000, 3000, 0),
        'char': MemorySegment(12000, 1000, 0),
        'string': MemorySegment(13000, 1000, 0),
        'Dataframe': MemorySegment(14000, 2000, 0),
    },
    'local': {
        'int': MemorySegment(16000, 2700, 0),
        'float': MemorySegment(18700, 2700, 0),
        'char': MemorySegment(21400, 900, 0),
        'string': MemorySegment(22300, 900, 0),
        'Dataframe': MemorySegment(23200, 1800, 0),
    },
    'constants': {
        'int': MemorySegment(25000, 2000, 0),
        'float': MemorySegment(27000, 2000, 0),
        'char': MemorySegment(28000, 1000, 0),
        'string': MemorySegment(29000, 1000, 0),
        'Dataframe': MemorySegment(30000, 1000, 0),
    }
}
function_directory = {}
params_directory = {}
current_scope = ['principal']
var_directory = [{}]
cte_directory = [{}]
quads = []
operators_stack = []
jump_stack = []
ids_stack = []
type_stack = []
jumps_stack = []
operators = ['+','-','*','/', ';'] #TODO: Implementar
temp_number = [0]
received_param_counter = [0]
scope = [None]
semantic_cube = semanticCube()
temp_var_counter = [VarCount(0,0,0,0,0)]

########## Utils ##########

def test():
  print("***************")
  print(ids_stack)
  print(type_stack)
  print("***************")

def addMigajitaDePan():
  jump_stack.append(len(quads))

def getVarCountFromType(var_type):
  if(var_type == "string"):
    return temp_var_counter[0].string_type
  elif(var_type == "int"):
    return temp_var_counter[0].int_type
  elif(var_type == "float"):
    return temp_var_counter[0].float_type
  elif(var_type == "char"):
    return temp_var_counter[0].char_type
  elif(var_type == "Dataframe"):
    return temp_var_counter[0].dataframe_type

def generateQuad(operator, left_operand, right_operand, temp_num, append_temp, result_type, scope):
  print(operator, left_operand, right_operand, temp_num, append_temp, result_type, scope)
  print(temp_var_counter[0])
  if not SHOW_VIRTUAL:
    if result_type and operator != 'escribe':
      generateAndAppendQuad(operator, left_operand, right_operand, "t{}{}".format(result_type[0], getVarCountFromType(result_type)), append_temp, result_type)
    else:
      generateAndAppendQuad(operator, left_operand, right_operand, None, append_temp, result_type)
  else:
    if not scope:
      generateAndAppendQuad(operator, left_operand, right_operand, temp_num, append_temp, result_type)
    else:
      generateAndAppendQuad(operator, left_operand, right_operand, getVirtualMemoryFrom(scope, result_type), append_temp, result_type)
  print(quads[len(quads) - 1])

def getVirtualMemoryFrom(scope, var_type):
  # print(scope, var_type)
  virtual_memory_cell = None
  if not SHOW_VIRTUAL:
    virtual_memory_cell = getVarCountFromType(var_type);
  else:
    virtual_memory_cell = virtual_memory[scope][var_type].setUsedSpace(getVarCountFromType(var_type))
  return virtual_memory_cell

########## Cuadruplos funciones ##########

def rememberBeginingOfFunction(function_name):
  # print("************** DIMELOOOU **************")
  temp_var_counter[0] = VarCount(0,0,0,0,0)
  function_directory[function_name].first_quad = len(quads);

def validateFunctionExistance(function_name):
  if function_name not in function_directory:
    raise EnvironmentError("""
          The function '{}' has not been declared.
        """.format(
          function_name,
        ))

def addVarToFunctionParams(var, function_name):
  # print(function_directory)
  # print(var)
  var_id = var[var.find(':')+1:]
  var_type = var[:var.find(':')]
  dimensions, var_id = getDimensions(var_id)
  function_directory[function_name].params.append(Variable(var_id, var_type, dimensions, getVirtualMemoryFrom('local', var_type)))

def incrementReceivedParamCounter():
  received_param_counter[0] += 1

def receivedFunctionParameters(function_name):
  # print("receivedFunctionParameters")
  # print(function_directory[function_name])
  # print(type_stack)
  temp_vars_table = {}
  type_stack_len = len(type_stack)
  ids_stack_len = len(ids_stack)
  if len(function_directory[function_name].params) != received_param_counter[0]:
    raise EnvironmentError("""
      The amount of params received when trying to call
      function '{}' is incorrect. Was expecting {} and received 
      {}.
    """.format(
      function_name,
      len(function_directory[function_name].params),
      received_param_counter[0]
    ))
  for i in range(0, len(function_directory[function_name].params)):
      definition_param = function_directory[function_name].params[
        len(function_directory[function_name].params) - 1 - i
      ]
      given_param_type = type_stack[type_stack_len - 1 - i]

      # print("Evaluating i={}".format(i))
      # print(definition_param.type, given_param_type)
      
      if definition_param.dimensions != {}:
        given_param_dimensions = function_directory['principal'].vars_table[ids_stack[ids_stack_len - 1 - i]].dimensions
        # print("{} vs {}".format(definition_param.dimensions, given_param_dimensions))

        if definition_param.dimensions != given_param_dimensions:
          raise EnvironmentError("""
            Given argument does not match the 
            parameter dimension of function '{}' - the argument #{} 
            does not have the same dimensions as the parameter declared
            in the function definition
          """.format(
            function_name,
            i + 1,
          ))

      if definition_param.type != given_param_type:
        raise EnvironmentError("""
          Given argument does not match the 
          parameter types of function '{}' - the argument #{} 
          was expecting type '{}' but received type '{}'
        """.format(
          function_name,
          len(function_directory[function_name].params) - i,
          definition_param.type,
          given_param_type
        ))
      
      # temp_vars_table[]
  received_param_counter[0] = 0
  # initializeVarsTable();

def insertERASize(function_name):
  generateQuad("ERA", function_name, None, None, False, None, None)

def initializeVarsTable():
  print("test")

def insertGOSUB(function_name):
  generateQuad("GOSUB", function_name, None, None, False, None, None)
  # Sólo si la función que estamos llamando regresa algo, hacemos el buen
  # PARCHE GUADALUPANO WUWUWUW
  if function_name in function_directory['principal'].vars_table:
    function_type = function_directory['principal'].vars_table[function_name].type
    generateQuad("=", function_name, None, getVarCountFromType(function_type), True, function_type, 'temporary')

########## Cuadruplos estatutos no lineales ##########

def addGotoF():
  # print(quads)
  exp_type = type_stack.pop()
  if exp_type != 'int':
    raise EnvironmentError("Type missmatch")
  operand = ids_stack.pop()
  generateQuad('GOTOF', operand, None, None, False, None, None)
  jump_stack.append(len(quads) - 1)

def addGotoA():
  last_goto_index = jump_stack.pop()
  generateQuad('GOTO', None, None, None, False, None, None)
  jump_stack.append(len(quads) - 1)    
  quads[last_goto_index].result_id = len(quads)

def addGotoPrincipal():
  generateQuad('GOTO', 'principal', None, None, False, None, None)

def addGotoEnd(origin):
  # print(jump_stack)
  last_goto_index = jump_stack.pop()
  if origin == 'while':
    quads[last_goto_index].result_id = jump_stack.pop()
  elif origin == 'si':
    quads[last_goto_index].result_id = len(quads)
  elif origin == 'for':
    # Decir que al finalizar el bloque for, re-evaluar la condición
    evaluation_index = jump_stack.pop()
    iterator_index = evaluation_index - 1
    generateQuad('+', quads[iterator_index].result_id, 1, quads[iterator_index].result_id, False, "int", 'local') #TODO: Verificar que iterador sea local
    generateQuad('GOTO', None, None, evaluation_index, False, None, None)
    # Decir que cuando N == M nos salimos del for
    quads[last_goto_index].result_id = len(quads)


def forEvaluation():
  # print("*******")
  # print(quads)
  # print()
  # print("*******")
  last_quad = quads[len(quads) - 1]
  type_stack.append('int')
  operators_stack.append('==')
  ids_stack.append(last_quad.result_id)
  leaving('comparacion')
  jump_stack.append(len(quads) - 1)
  generateQuad('GOTOV', ids_stack.pop(), None, None, False, None, None)
  jump_stack.append(len(quads) - 1)

########## Cuadruplos estatutos lineales ##########

def insertCteToStructs(cte, cte_type):
  type_stack.append(cte_type)
  if (cte):
    cte_directory[0][str(cte)] = Constant(cte, cte_type, getVirtualMemoryFrom('constants', cte_type))

def insertCteToStack(cte):
  ids_stack.append(cte)

def insertIdToStack(identificator):
  # print('insertIdToStack {}'.format(identificator))
  # Busca en donde está esta variable...
  if identificator in function_directory['principal'].vars_table: # Global
    type_stack.append(function_directory['principal'].vars_table[identificator].type)
    ids_stack.append(identificator)
  elif identificator in function_directory[current_scope[0]].vars_table: # Current scope
    type_stack.append(function_directory[current_scope[0]].vars_table[identificator].type)
    ids_stack.append(identificator)
  else:
    raise EnvironmentError("Hubo un error al intentar utilizar '{}' ¿Tal vez no fue declarado?".format(identificator))
    quit()
    

def insertOperator(operator):
  operators_stack.append(operator)

def deleteParenthesis():
  operators_stack.pop()

def insertParenthesis():
  operators_stack.append('(')

def leaving(origin):
  allowed_operators = None
  if origin == 'factor':
    allowed_operators = ['*', '/']
  elif origin == 'termino':
    allowed_operators = ['+', '-']
  elif origin == 'comparacion':
    allowed_operators = ['>', '<', '>=', '<=', '==', '!=']
  elif origin == 'union':
    allowed_operators = ['&', '|']
  elif origin == 'asignacion':
    allowed_operators = ['=']

  if len(operators_stack) >= 1 and len(ids_stack) >= 2 and operators_stack[len(operators_stack) - 1] in allowed_operators:
      operator = operators_stack.pop()
      right_operand = ids_stack.pop()
      right_operand_type = type_stack.pop()
      left_operand = ids_stack.pop()
      left_operand_type = type_stack.pop()
      # print("{} ({}) {} {} ({})".format(
      #   left_operand,
      #   left_operand_type,
      #   operator,
      #   right_operand,
      #   right_operand_type,
      # ))
      result_type = semantic_cube.cube[left_operand_type][operator][right_operand_type]
      if 'Error:' in result_type:
        raise EnvironmentError(result_type[7:])
      if (origin != 'asignacion'):
        # print("{} {} {} = {}".format(left_operand, operator, right_operand, result_type))
        generateQuad(operator, left_operand, right_operand, getVarCountFromType(result_type), True, result_type, 'temporary')
        insertCteToStructs(None, result_type)
      else:
        generateQuad(operator, right_operand, None, left_operand, False, result_type, 'local') #TODO: Verificar que esto sea correcto

def readId(identificator):
  generateQuad('lee', identificator, None, getVarCountFromType('string'), False, "string", 'temporary')
  type_stack.pop()

def write(id_or_cte):
  #TODO: Necesitamos traducir estas id's y CTE's a memory cells
  if id_or_cte:
    generateQuad('escribe', id_or_cte, None, None, False, "string", None)
  else:
    generateQuad('escribe', ids_stack.pop(), None, None, False, "string", None)
  type_stack.pop()

def generateReturnQuad(megaexpresion):
  # print(megaexpresion)
  megaexpresion_return_type = None
  return_value = None
  if (any(operator in megaexpresion for operator in operators)): # Operation
    # print("operation found")
    # print(quads)
    # print(ids_stack)
    # print(type_stack)
    return_value = ids_stack[len(ids_stack) - 1]
    megaexpresion_return_type = type_stack[len(type_stack) - 1]
  elif ('(' in megaexpresion): # Function
    called_function = megaexpresion[: megaexpresion.find('(')]
    megaexpresion_return_type = function_directory['principal'].vars_table[called_function].type
    return_value = called_function
  else: # CTE or ID
    # print("cte or id found")
    if (megaexpresion in cte_directory[0]): #cte
      # print("it's a constantttt")
      megaexpresion_return_type = cte_directory[0][megaexpresion].type
    elif (megaexpresion in function_directory[current_scope[0]].vars_table):
      # print("it's a local id")
      megaexpresion_return_type = function_directory[current_scope[0]].vars_table[megaexpresion].type
    elif (megaexpresion in function_directory['principal'].vars_table):
      # print("it's a global id")
      megaexpresion_return_type = function_directory['principal'].vars_table[megaexpresion].type
    else:
      raise EnvironmentError("The CTE or ID that was intended to return was not found. Perhaps it hasn't been declared yet?")
      quit()
    # print("assigning...")
    return_value = megaexpresion
  if (megaexpresion_return_type == function_directory['principal'].vars_table[current_scope[0]].type):
    generateQuad('RETURN', None, None, return_value, False, megaexpresion_return_type, None)
  else:
    raise EnvironmentError("""
        The return type the function '{}' expected was '{}' but received '{}'.
      """.format(
        current_scope[0],
        function_directory['principal'].vars_table[current_scope[0]].type,
        megaexpresion_return_type
      ))

def generateAndAppendQuad(operator, left_operand, right_operand, temp_num, append_temp, result_type):
  if 'GOTO' in operator:
    new_quad = Quad(operator, left_operand, right_operand, temp_num)
    quads.append(new_quad)
  else:
    if type(temp_num) == str: # No asignacion
      new_quad = Quad(operator, left_operand, right_operand, temp_num)
    else: # Asignacion
      new_quad = Quad(operator, left_operand, right_operand, temp_num)
    quads.append(new_quad)
    if append_temp:
      ids_stack.append(temp_num)
    if type(temp_num) == str:
      temp_var_counter[0].increment(result_type)

def getDimensions(var_id):
  id_string = str(var_id)
  dimensions = {}
  if id_string.count('[') == 1:
    dimensions['1'] = int(id_string[id_string.find('[') + 1:id_string.find(']')])
    id_string = id_string[:id_string.find('[')]
  elif id_string.count('[') == 2:
    dimensions['1'] = int(id_string[id_string.find('[') + 1:id_string.find(']')])
    dimensions['2'] = int(id_string[id_string.rfind('[') + 1:id_string.rfind(']')])
    id_string = id_string[:id_string.find('[')]
  return dimensions, id_string

def addVarToVarsTable(var_type, var_id, last_var):
  # print(var_id, var_type)
  if var_id in function_directory: # It's a function's id
      raise EnvironmentError("""
        The id '{}' has already been declared as a function.
      """.format(
        var_id
      ))
  elif not last_var:
    final_type = var_type
  else:
    final_type = last_var[:last_var.find(':')]
  dimensions, id_string = getDimensions(var_id)
  var_directory[0][id_string] = Variable(id_string, final_type, dimensions, getVirtualMemoryFrom('local', final_type))


def setScope(id):
  current_scope[0] = id

def addFunctionToDirectory(function_id, function_type):
  function_directory[function_id] = Function(function_id, function_type, [], None, None, {})
  if function_type:
    function_directory['principal'].vars_table[function_id] = Variable(function_id, function_type, {}, getVirtualMemoryFrom('global', function_type))

def includeVarsTableInFunction(id):
  function_directory[id].vars_table = var_directory[0]
  var_directory[0] = {}

def getCellCount(dimensions):
  cells = 1
  for dimension in dimensions:
    cells *= dimensions[dimension]
  return cells

def getVarCount(dimensions):
  if dimensions == {}:
    return 1
  else:
    return getCellCount(dimensions)

def getVarCountFromVarsTable(vars_table):
  int_counter = 0
  float_counter = 0
  char_counter = 0
  string_counter = 0
  dataframe_counter = 0

  for key in vars_table:
    var_type = vars_table[key].type
    var_dimensions = vars_table[key].dimensions
    if var_type == 'int':
      int_counter += getVarCount(var_dimensions)
    elif var_type == 'float':
      float_counter += getVarCount(var_dimensions)
    elif var_type == 'char':
      char_counter += getVarCount(var_dimensions)
    elif var_type == 'string':
      string_counter += getVarCount(var_dimensions)
    elif var_type == 'Dataframe':
      dataframe_counter += 1
  
  return VarCount(
    int_counter,
    float_counter,
    char_counter,
    string_counter,
    dataframe_counter,
  )

def reachedFunctionDefinitionEnd(id):
  # Save ERA Size on function_directory
  function_directory[id].var_count = getVarCountFromVarsTable(function_directory[id].vars_table) + temp_var_counter[0]
  # Release varstable
  function_directory[id].vars_table = {}
  # Generate ENDFUNC quad
  generateQuad('ENDFUNC', None, None, None, False, None, None)
  # Reset temp_number
  
  temp_number[0] = 0