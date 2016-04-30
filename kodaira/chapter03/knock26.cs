/*
 * Chapter03, knock26
 * Task: Remove Markup
 * Compile: mcs /reference:***.DLL ***.cs
 */

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using System.IO.Compression;
using System.Net;
using System.Text;

using BasicInfomationExtraction;

public class Knock26 {
    static public void Main(string[] args) {
        Dictionary<string, string> dict = Knock25.ExtractTarget(args[0]);
        foreach (KeyValuePair<string, string> kv in dict) {
            Console.WriteLine(string.Format("{0}: {1}", kv.Key, RemoveMarkup(kv.Value)));
        }
            
    }
    public static string RemoveMarkup(string s, string target="'''") {
        return s.Replace(target, "");
    }

}

