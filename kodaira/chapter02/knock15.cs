/*
 * Chapter02, knock15
 * Task: tail
 *       Unix Command ``tail''
 */

using System;
using System.IO;
using System.Collections.Generic;

public class Knock15 {
    static public void Main(string[] args) {
        Tail(args[0], Int32.Parse(args[1]));
    }

    public static void Tail(string path, int num=10) {
        string[] lines = File.ReadAllLines(path);
        int start = lines.Length - num;
        for (int i=start; i < lines.Length; i++) {
            Console.WriteLine(lines[i]);
        }
    }
}

