/*
 * Chapter02, knock16
 * Task: split
 *       Unix Command ``split''
 */

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;

public class Knock16 {
    static public void Main(string[] args) {
        Split(args[0], Int32.Parse(args[1]));
    }

    public static void Split(string path, int num=2) {
        string[] lines = File.ReadAllLines(path);
        int under = lines.Length / num, amari = lines.Length % num;
        int[] nums = Enumerable.Repeat<int>(under, num).ToArray();
        int index = 0, nokori = nums[0];
        StreamWriter sw = File.CreateText(string.Format("./data/split{0}.txt", index));
        for (int i=0; i < amari; i ++) { nums[i] ++; }
        for (int i=0; i < lines.Length; i++) {
            sw.WriteLine(lines[i]);
            if (--nokori == 0) {
                sw.Close();
                if (++index != num) {
                    sw = File.CreateText(string.Format("./data/split{0}.txt", index));
                    nokori = nums[index];
                }
            }
        }
    }
}

