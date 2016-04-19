/*
 * Chapter01, knock09
 * Task: Make Typoglycemia Sentence.
 */

using System;
using System.Linq;


public class TypoglycemiaSentence {
    static public void Main() {
        string sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .";
       
        Console.WriteLine(Typoglycemia(sentence));
    }


    public static string Typoglycemia(string str, string d=" ") {
        string[] delimiter= new string[] {d};
        string[] words =  str.Split(delimiter, StringSplitOptions.None);
        string typoglycemiaSentence = "";
        for (int i=0; i < words.Length; i++) {
            int wordLength = words[i].Length;
            if (wordLength > 4) {
                typoglycemiaSentence += words[i][0] + ShuffleString(words[i].Substring(1,  wordLength - 2)) + words[i][wordLength-1]; 
            } else {
                typoglycemiaSentence += words[i];
            }
            if (i != words.Length-1)
                typoglycemiaSentence += " ";
        }
        return typoglycemiaSentence;
    }


    public static string ShuffleString(string str) {
        Random rand = new Random();
        return new string(str.ToCharArray().
                OrderBy(s => (rand.Next(2) % 2) == 0).ToArray());
    }
}

