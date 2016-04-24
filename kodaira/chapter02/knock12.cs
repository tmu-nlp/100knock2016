/*
 * Chapter02, knock12
 * Task: extract one column
 *       Unix Command ``cut''
 */

using System;
using System.IO;
using System.Collections.Generic;

public class Knock12 {
    static public void Main(string[] args) {
        int[] nums = new int[] {0, 1};
        ExtractColumn(args[0], nums);
    }

    public static void ExtractColumn(string path, int[] nums) {
        Dictionary<int, StreamWriter> fout = new Dictionary<int, StreamWriter>();
        char [] deli = new char [] {'\t', '\n'};

        foreach (int num in nums) {
            fout[num] = File.CreateText(string.Format("./data/col{0}.txt", num));
        }

        using (StreamReader sr = File.OpenText(path)) {
            string line = "";
            while ((line = sr.ReadLine()) != null) {
                string [] split = line.Split(deli);
                foreach (KeyValuePair<int, StreamWriter> num_fout in fout) {
                    num_fout.Value.WriteLine(split[num_fout.Key]);
                }   
            }
        }
        foreach (KeyValuePair<int, StreamWriter> num_fout in fout) {
            num_fout.Value.Close();
        }   
    }
}

