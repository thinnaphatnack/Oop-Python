องค์ประกอบพื้นฐานในภาษาเชิงวัตถุ
   1. ต้นแบบของวัตถุ(Class) & วัตถุ (Object) 
*ชื่อ class ควรตั้งเป็น คำนาม ขึ้นต้นด้วยตัวอักษรพิมพ์ใหญ่ ถ้าประกอบด้วยคำมากว่า 1 คำ ให้ตัวขึ้นต้นแต่ละคำด้วยอักษรพิมพ์ใหญ่เขียนติดกัน ห้ามเว้นวรรค หลีกเลี้ยงการใช้เครื่องหมาย _ คั่น
Ex. class Home : 

Object คือสิ่งที่ถูกสร้างขึ้นมาจาก Class ประกอบด้วย 2 คุณสมบัติคือ
    ●คุณสมบัติ/คุณลักษณะ Attribute *คำนาม/คำวิเศษณ์
*ชื่อ Attribute ควรเป็นคำนามหรือคำวิเศษณ์และขึ้นต้นด้วยอักษรตัวพิมพ์เล็กถ้าประกอบด้วยคำมากกว่า 1 คนให้คำหลังขึ้นต้นด้วยอักษรตัวพิมพ์ใหญ่เขียนติดกันห้ามเว้นวรรค หลีกเลี้ยงการใช้เครื่องหมาย _ คั้น
Ex. self.name = name

    ●พฤติกรรม Behavior & Method (Function) *คำกริยา
ชื่อ Method ควรเป็นคำกริยา และขึ้นต้นด้วยอักษรพิมพ์เล็ก ถ้าประกอบด้วยคำมากว่า 1 คำ ให้คำหลังขึ้นต้นด้วยตัวอักษรพิมพ์ใหญ่ เขียนติดกัน ห้ามเว้นวรรค หลีกเลี้ยงการใช้เครื่องหมาย _ คั้น
Ex. def runNing(self):

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
การสืบทอดคือ การสร้างสิ่งใหม่ขึ้นด้วยการสืบทอดหรือรับเอา(inherit)คุณสมบัติบางอย่างมาจากสิ่งเดิมที่มีอยู่แล้วโดยการสร้างเพิ่มเติมจากสิ่งที่มีอยู่แล้วได้เลย *ยกเว้น Private Attribute & Private Method
คลาสแม่ (Superclass) , คลาสลูก (Subclass)
การสืบทอดคุณสมบัติ
คลาสแม่
class Employee :
คลาสลูก
class Programmer(Employee):

คีย์เวิร์ด Super
เมื่อต้องการเรียกใช้งานคุณสมบัติต่างๆในคลาสแม่ เช่น Constructor , Method , Attribute จะใช้คีย์เวิร์ด >> super().__init__(name)

การแปลง Object เป็น String
def __str__(self):
   return "ชุดข้อความ"
   
    3.การพ้องรูป  ( Polymorphism )
Polymorphism เกิดจาก poly (หลากหลาย) + morphology (รูปแบบ)
ในทางโปรแกรมคือการที่เมธอดชื่อเดียวกัน สามารถรับอาร์กิวเมนต์ที่แตกต่างกันได้หลายรูปแบบ โดยเมธอดนี้จะถูกเรียกว่า overload method (เมธอดถูกโอเวอร์โหลด)
Polymorphism "ข้อความเดียวกันแต่กระบวนการทำงานภายในแตกต่างกัน นั้นเรียกว่า การพ้องรูป หรือ polymorphism"

Overloading method
คือ Method ที่มีชื่อเหมือนกันและอยู่ในคลาสเดียวกัน สิ่งที่แยกความแตกต่างของ method ที่เป็น overload method คือ พารามิเตอร์ (เป็นผลมาจากคุณสมบัติ oo คือ polymorphism)

Overriding method
คือ Method ของคลาสลูก (subclass) ที่มีชื่อเหมือนกับ method ของคลาสแม่ (superclass) (เป็นผลมาจากคุณสมบัติ oo คือ inheritance)

ฟังก์ชั่นที่ทำงานกับ Class และ Object 
isinstance : เช็กว่า Object นี้ถูกสร้างจาก Class ที่เรานิยามหรือไม่
dir              : แสดง Attribute และ Method
__clsss__ : แสดงชื่อ class และ object

self คือคีย์เวิร์ดที่ใช้สำหรับอ้างอิงถึงตัวแปรที่อยู่ภายในคลาสเพื่อให้แตกต่างจากชื่อ Attribute 

Static
ในภาษา Python Attribute (ตัวแปร) ใน Class จะเป็น Static อยู่แล้ว สามารถเรียกใช้งานผ่าน "ชื่อคลาส.ชื่อตัวแปร" ได้เลย
แต่สำหรับ Method นั้นถ้าต้องการกำหนดให้เป็น Method แบบ Static ต้องไม่ใส่คีย์เวิร์ด self ไว้ในพารามิเตอร์

if __name__ == '__main__' : คือการตรวจสอบว่าคำสั่งที่รันอยู่ภายใน __main__ มาจากคลาสที่อยู่ในไฟล์ หรือ โมดูลเดียวกันหรือไม่
ช่วยให้เลือกรันหรือไม่รันโค้ดในไฟล์ที่ต้องการได้
