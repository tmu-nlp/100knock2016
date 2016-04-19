/*
 * Chapter01, knock08
 * Task: Cipher Function (reverse alphabet e.g. a -> z, b ->y ).
 */

using System;

public class TemplateGeneration {
    static public void Main () {
        string password = "aBcxYz";
        
        Console.WriteLine("Password: {0}", password);
        Console.WriteLine("Decode: {0}", Cipher(password));
        Console.WriteLine("Encode: {0}", Cipher(Cipher(password)));
    }

    static string Cipher(string str) {
        string code = "";
        foreach(char c in str) {
            if (!char.IsLower(c)) code += c;
            else code += (char)(219 - c);
        }
        return code;
    }
}
