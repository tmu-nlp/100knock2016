/*
 * Chapter03, knock25
 * Task: Extract Basic Information and store their
 * Compile: mcs /target:library /out:***.DLL *.cs
 */

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using System.IO.Compression;
using System.Net;
using System.Text;


namespace BasicInfomationExtraction {
    public class Knock25 {
        static public void Main(string[] args) {
            Dictionary<string, string> dict = ExtractTarget(args[0]);
            foreach (KeyValuePair<string, string> kv in dict) {
                Console.WriteLine(string.Format("{0}: {1}", kv.Key, kv.Value));
            }
                
        }

        public static Dictionary<string, string> ExtractTarget(string path, string target="{{基礎情報") {
            bool fi_flag = false;
            Dictionary<string, string> dict = new Dictionary<string, string>();
            
            char []deli = new char []{'\t'};
            using (StreamReader sr = File.OpenText(path)) {
                string line = "";
                while ((line = sr.ReadLine()) != null) {
                    if (fi_flag && line == "}}") fi_flag = false; 
                    if (fi_flag) {
                        string fi = (System.Text.RegularExpressions.Regex.Replace(line, @"\|(.*) =(.*)$", "$1\t$2"));
                        string []split = fi.Split(deli);
                        dict[split[0]] = split[1];
                    }
                    if (System.Text.RegularExpressions.Regex.IsMatch(line, target)) fi_flag = true; 
                }
            }
            return dict;

        }
    }
}
