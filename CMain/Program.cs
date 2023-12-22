using System;

namespace CMain //foldaer name, must be same!!!!!
{
    class Program // dont know
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Key: ");
            var key = Console.ReadKey();
            var love = "json";
            Console.WriteLine(key);
            
            if (key.Equals(love))
            {
                Console.WriteLine("ok");

            }
            else
            {
                Console.WriteLine("Unkown user");

            }
            
            
            Console.ReadKey();
            
         
        }
    }
}