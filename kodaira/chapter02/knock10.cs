/*
 * Chapter02, knock10
 * Task: count row in text file.
 *       Unix Command ``wc''
 */

using System;
using System.IO;

public class Knock10 {
    static public void Main(string[] args) {
       Console.WriteLine(RowCount(args[0]));
    }

    public static int RowCount(string path) {
        int count = 0;
        using (StreamReader sr = File.OpenText(path)) {
            while ((sr.ReadLine()) != null) {
                count ++;
            }
        }
        return count;
    }
}

