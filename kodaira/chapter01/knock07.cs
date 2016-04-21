/*
 * Chapter01, knock07
 * Task: Make Template.
 */

using System;

public class TemplateGeneration {
    static public void Main () {
        Console.WriteLine(Template(12, "気温", 22.4));
    }

    static string Template(int hour, string unit, double value) {
        return String.Format("{0}時の{1}は{2}ですです．", hour, unit, value);
    }
}
