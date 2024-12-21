using System;

 class prog{
    static void Main()
    {
        try
        {
            Console.Write("Enter the first number: ");
            double num1= double.Parse(Console.ReadLine());


            Console.Write("Enter the second number: ");
            double num2 = double.Parse(Console.ReadLine());


            Console.Write("Choose operation (+, -, *, /):   ");
            string oper = Console.ReadLine();

            Console.WriteLine();


            if (oper == "+")
            {
               Console.WriteLine( Add(num1 , num2));
            }
            else if (oper == "-")
            {
                Console.WriteLine(Subtract(num1, num2));
            }
            else if (oper == "*")
            {
                Console.WriteLine(multiply(num1, num2));
            }
            else if (oper =="/")
            {
                if (num2 != 0)
                {
                    Console.WriteLine(divide(num1, num2));
                }
                else
                {
                    Console.WriteLine("Error you can not Division by zero");
                }
            }
            else
            {
                Console.WriteLine("wrong operation");
            }
        }
        catch (DivideByZeroException)
        {
            Console.WriteLine("Error you can not Division by zero");
        }
        catch (NullReferenceException ex)
        {
            Console.WriteLine("Error you can not write null value");
            Console.WriteLine(ex.Message);
        }
        catch (FormatException formatEx)
        {
            Console.WriteLine("Error you Entered string value which is wrong");
            Console.WriteLine(formatEx.Message);
        }
        catch (Exception ex)
        {
           
            Console.WriteLine("Exception Message => " + ex.Message);
            Console.WriteLine("Exception Details => " + ex.StackTrace);
            Console.WriteLine("Exception Details => " + ex.ToString());
        }
       

    }

    static double Add(double a, double b)
    {
        return a + b;
    }
    static double Subtract (double a, double b)
    {
        return a - b;
    }
    static double multiply(double a, double b)
    {
        return a * b;
    }
    static double divide(double a, double b)
    {
        return a / b;
    }






}

