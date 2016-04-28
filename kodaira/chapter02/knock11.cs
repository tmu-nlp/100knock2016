/*
 * Chapter02, knock11
 * Task: replace tabspace to one space.
 *       Unix Command ``sed'' or ``tr'' or ``expand''
 */

using System;
using System.IO;

public class Knock11 {
    static public void Main(string[] args) {
       ReplaceDelimiter(args[0]);
    }

    public static void ReplaceDelimiter(string path) {
        using (StreamReader sr = File.OpenText(path)) {
            string line = "";
            while ((line = sr.ReadLine()) != null) {
                Console.WriteLine(line.Replace('\t', ' '));
            }
        }
    }
}

