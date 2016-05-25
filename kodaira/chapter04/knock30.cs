/*
 * chapter4, knock 30
 * Task: Using mecab
 *  extract surface, base, pose, pos1
 *
 * Compile: mcs /reference:LibNMeCab.dll **.cs
 */


using System;
using System.IO;
using System.Collections.Generic;

using NMeCab;

namespace NMecab {
    public class Knock30 {
        static public void Main(string[] args) {
            MeCabTagger tagger = GetParser();
            ParseSentences(args[0], tagger);

        }

        public static MeCabTagger GetParser() {
            MeCabParam param = new MeCabParam();
            param.DicDir = @"ipadic";

            MeCabTagger tagger = MeCabTagger.Create(param);
            return tagger;
        }

        public static void ParseSentences(string path, MeCabTagger tagger) {
            using (StreamReader sr = File.OpenText(path)) {
                string line = "";
                MeCabNode node = tagger.ParseToNode("");
                while ((line = sr.ReadLine()) != null) { 
                    node = tagger.ParseToNode(line);
                    while (node != null) {
                        if (node.CharType > 0) {
                            Console.Write(node.Surface);
                            Console.Write("_");
                        }
                        node = node.Next;
                    }
                    break;
                }
            }
        }
    }
}
