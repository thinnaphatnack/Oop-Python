องค์ประกอบพื้นฐานในภาษาเชิงวัตถุ
   1. ต้นแบบของวัตถุ(Class) & วัตถุ (Object)
Object คือสิ่งที่ถูกสร้างขึ้นมาจาก Class ประกอบด้วย 2 คุณสมบัติคือ
    ●คุณสมบัติ/คุณลักษณะ    
        Attribute *คำนาม
self.name = name
    ●พฤติกรรม    
        Behavior & Method (Function) *คำกริยา
def getName(self):

คุณสมบัติของการเขียนโปรแกรมเชิงวัตถุ
    1.การห่อหุ้ม   ( Encapsulation )
  Access Modifier ระดับในการเข้าถึง Class , Attribute , Method
  Public             : ทุก Class สามารถเข้าถึงได้
  Protected (_) : Class ของตัวเองและ Class ลูกที่สืบทอดคุณสมบัติเท่านั้นที่จะเข้าถึงได้
  Private ( __ )  : จะมีเฉพาะ Class ตัวเองเท่านั้นที่เข้าถึงได้
  
  Setter ,  Getter Method

    2.การสืบทอด ( Inheritance )
    3.การพ้องรูป  ( Polymorphism )


เขียนโปรแกรม
ชื่อ Class ตัวแรกควรเป็นตัวพิมพ์ใหญ่
ชื่อ Function ควรเป็นพิมพ์เล็กทั้งหมด

ฟังก์ชั่นที่ทำงานกับ Class และ Object 
isinstance : เช็กว่า Object นี้ถูกสร้างจาก Class ที่เรานิยามหรือไม่
dir              : แสดง Attribute และ Method
__clsss__ : แสดงชื่อ class และ object
