using System;
using System.Collections.Generic;
using System.Text.Json;

namespace GithubDesktopZhTool
{
    public class main
    {
        public string Name { get; set; }
        public string Version { get; set; }
        public List<string> Items { get; set; }

        public main()
        {
            Name = "GithubDesktopZhTool";
            Version = "1.0.0";
            Items = new List<string> { "Item1", "Item2", "Item3" };
        }

        public void Run()
        {
            Console.WriteLine($"Welcome to {Name} v{Version}");
            Console.WriteLine("Items:");
            foreach (var item in Items)
            {
                Console.WriteLine($"- {item}");
            }
        }

        public string ToJson()
        {
            return JsonSerializer.Serialize(this, new JsonSerializerOptions
            {
                WriteIndented = true
            });
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var app = new main();
            app.Run();
            Console.WriteLine("\nJSON Output:");
            Console.WriteLine(app.ToJson());
        }
    }
}

# Code Update 1760523672-30168

# Code Update 1760523672-21328

# Code Update 1760523672-7448

# Additional Implementation 1760523672

# Code Update 1760523672-7086

# Additional Implementation 1760523673

# Code Update 1760523673-8687

# Additional Implementation 1760523673

# Code Update 1760523673-14709

# Additional Implementation 1760523674

# Code Update 1760523674-1889
