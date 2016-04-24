/*
 * Chapter02, knock14
 * Task: head 
 *       Unix Command ``head''
 */

using System;
using System.IO;
using System.Collections.Generic;

public class Knock14 {
    static public void Main(string[] args) {
        Head(args[0], Int32.Parse(args[1]));
    }

    public static void Head(string path, int num) {
        int count = 0;
        using (StreamReader sr = File.OpenText(path)) {
            string line = "";
            while ((line = sr.ReadLine()) != null) {
                Console.WriteLine(line);
                if (++count == num) { break; }
            }
        }
    }
}

