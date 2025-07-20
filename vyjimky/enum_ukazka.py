from enum import Enum

class Jazyk(Enum):
   CSHARP = "C#"
   JAVA = "Java"
   PHP = "PHP"
   PYTHON = "Python"

# Použití
jazyk = Jazyk.JAVA

print(jazyk.value)