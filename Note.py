องค์ประกอบพื้นฐานในภาษาเชิงวัตถุ
   1. ต้นแบบของวัตถุ(Class) & วัตถุ (Object)
Object คือสิ่งที่ถูกสร้างขึ้นมาจาก Class ประกอบด้วย 2 คุณสมบัติคือ
    ●คุณสมบัติ/คุณลักษณะ Attribute *คำนาม
Ex. self.name = name
    ●พฤติกรรม Behavior & Method (Function) *คำกริยา
Ex. def getName(self):

คุณสมบัติของการเขียนโปรแกรมเชิงวัตถุ
    1.การห่อหุ้ม   ( Encapsulation )
  Access Modifier ระดับในการเข้าถึง Class , Attribute , Method
  Public             : ทุก Class สามารถเข้าถึงได้
  Protected (_)      : Class ของตัวเองและ Class ลูกที่สืบทอดคุณสมบัติเท่านั้นที่จะเข้าถึงได้
  Private ( __ )     : จะมีเฉพาะ Class ตัวเองเท่านั้นที่เข้าถึงได้
  
Setter ,  Getter (Method)
   Setter การกำหนดค่าให้กับ Objet
Ex. def SetName(self,newname):
      self.__name = newname
   Getter การดึงค่าจาก Object
Ex. def getName(self):
      return self.__name

Class Variable & Instance Variable
- Class Variable    คือ ตัวแปลที่ทำงานภายใน Class ส่วนอื่นสามารถเข้าถึงข้อมูลนี้ได้เลย ( Static attrbiute ) โดยไม่จำเป็นต้องสร้าง Object ขึ้นมา *เข้าถึงได้เฉพาะ Public และ Protected
- Instance Variable คือ ตัวแปลที่อยู่ภายใน Object สามารถเข้าถึงข้อมูลส่วนนี้โดยการต้องสร้าง Object ขึ้นมา
Ex.Class Employee :
   # Class variable
   _minSalary = 1000
   _maxSalary = 5000
      def __init__(self,name,salary,department):
            # Instance Variable
            self.__name = name
            self.__salary = salary
            self.__department = department

    2.การสืบทอดคุณสมบัติ ( Inheritance )
การสืบทอดคือ การสร้างสิ่งใหม่ขึ้นด้วยการสืบทอดหรือรับเอา(inherit)คุณสมบัติบางอย่างมาจากสิ่งเดิมที่มีอยู่แล้วโดยการสร้างเพิ่มเติมจากสิ่งที่มีอยู่แล้วได้เลย
    3.การพ้องรูป  ( Polymorphism )


เขียนโปรแกรม
ชื่อ Class ตัวแรกควรเป็นตัวพิมพ์ใหญ่
ชื่อ Function ควรเป็นพิมพ์เล็กทั้งหมด

ฟังก์ชั่นที่ทำงานกับ Class และ Object 
isinstance : เช็กว่า Object นี้ถูกสร้างจาก Class ที่เรานิยามหรือไม่
dir              : แสดง Attribute และ Method
__clsss__ : แสดงชื่อ class และ object
