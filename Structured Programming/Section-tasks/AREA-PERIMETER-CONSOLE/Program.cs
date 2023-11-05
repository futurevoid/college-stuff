Console.WriteLine("Enter The Length:");
int length  = int.Parse(Console.ReadLine());
Console.WriteLine("");
Console.WriteLine("Enter The Width:");
int width  = int.Parse(Console.ReadLine());
int area = length * width;
int perimeter = (width +length) * 2;
Console.WriteLine($"Area: {area}");
Console.WriteLine($"Perimeter: {perimeter}");
