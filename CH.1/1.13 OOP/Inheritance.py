# https://runestone.academy/runestone/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#inheritance-logic-gates-and-circuits

class LogicGate:
    """At the top of the hierarchy, the LogicGate class represents the most general characteristics of logic gates - namely, a label for the gate and an output line.
    
                        Logic Gate
                            |
                           / \
                Binary Gate   Unary Gate
                      |            |
                     / \           |
             AND -connnector- OR  NOT
                        
    """
    def __init__(self, label):
        """Constructor definition
        
        Each gate has a label for identification and a single output line. Every logic gate also needs an ability to know its boolean output value.
        """
        self.label = label
        self.output = None

    def getLabel(self):
        """Returns label"""
        return self.label

    def getOutput(self):
        """"Returns output"""
        self.output = self.performGateLogic()
        # 
        return self.output

class BinaryGate(LogicGate):
    """A child class, BinaryGate. It inherits all of LogicGate's attributes"""
    
    def __init__(self, label):
        # We start with an explicit call to the constructor of the parent class using the parent's __init__ method. When creating an instance of the BinaryGate class, we first want to initialize any data items that are inherited from LogicGate (in this case, the label for the gate). 
        LogicGate.__init__(self, label)

        # Child class constructors need to call parent class constructors and then move on to their own distinguishing data (in this case, the two input lines below).
        self.pinA = None
        self.binB = None

    def getPinA(self):
        return int(input(f"Enter pin A input for gate {self.getLabel()}: "))

    def getPinB(self):
        return int(input(f"Enter pin B input for gate {self.getLabel()}: "))

class UnaryGate(LogicGate):
    """A child class of LogicGate"""

    def __init__(self, label):
        """Note:
        
        LogicGate.__init__(self, lbl) could be replaced with super().__init__(lbl), super(UnaryGate, self).__init__(lbl), or super().__init__("UnaryGate", lbl)
        """
        LogicGate.__init__(self, label)
        self.pin = None

    def getPin(self):
        return int(input(f"Enter pin input for gate {self.getLabel()}"))

class AndGate(BinaryGate):
    """A child class of BinaryGate"""

    def __init__(self, label):
        super().__init__(label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    """A child class of BinaryGate"""

    def __init__(self, label):
        super().__init__(label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if ((a == 1 and b == 0) or (a == 0 and b == 1)):
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    """A child class of UnaryGate"""

    def __init__(self, label):
        super().__init__(label)
    
    def performGateLogic(self):
        a = self.getPin()
        
        if a == 1:
            return 0
        else:
            return 1

class Connector:
    """Connector Has-a LogicGate
    
    The Connector class does not reside in the gate hierarchy, but will use it in that each connector will have two gates - one on the either end. This relationship is called the Has-a relationship:

                        from           to
                        gate           gate
                   AND ----> connector ----> OR
                (AndGate)                  (OrGate)

    With the Connector class, we say that a Connector Has-a LogicGate, meaning that connectors will have instances of the LogicGate class within them but are not part of the hierarchy.
    Note that there is also a Is-a relationship which requires inheritance (e.g. UnaryGate is a LogicGate while Connector has a LogicGate). Has-a relationships do not require inheritance
    """

    def __init__(self, fgate, tgate):
        """Constructor setup

        Param 
            - fromGate: an AndGate object which represents the leftend of the flow from output of one gate into an input line of the next
            - toGate: and AndGate object which represents the righthand of the flow described above 
        """
        self.fromGate = fgate
        self.toGate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

    def getPinA(self):
        if self.pinA == None:
            return input(f"Enter pin A input for gate {self.getLabel()}")
        else:
            return self.pinA.getFrom().getOutput()

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

g4.getOutput()