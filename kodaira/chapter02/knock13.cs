/*
 * Chapter02, knock13
 * Task: merge two column
 *       Unix Command ``paste''
 */

using System;
using System.IO;
using System.Collections.Generic;

public class Knock13 {
    static public void Main(string[] args) {
        MeargeColumn(args);
    }

    public static void MeargeColumn(string[] paths) {
        using (StreamReader sr1 = File.OpenText(paths[0]), sr2 = File.OpenText(paths[1])) {
            string line1 = "", line2 = "";
            using (StreamWriter sw = File.CreateText("./data/col12.txt")) {
                while ((line1 = sr1.ReadLine()) != null && (line2 = sr2.ReadLine()) != null) {
                    sw.WriteLine(string.Format("{0}\t{1}", line1, line2));
                }   
            }
        }
    }
    
}

