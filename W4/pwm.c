//设定使用9号口
void setup (){
pinMode(9,OUTPUT);
}
void loop(){
//由于上文中提到的所以为256种亮度
for (int a=0; a<=255;a++) //控制PWM亮度的增加 
{
analogWrite(9,a); 
delay(8); 
} 
for (int a=255; a>=0;a--) /／控制PWM亮度减小 
{ 
analogWrite(9,a); 
delay(8); 
} 
delay(300); //完成一个循环
}