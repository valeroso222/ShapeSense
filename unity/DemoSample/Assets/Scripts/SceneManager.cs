using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEngine;
using UnityEngine.UI;

public enum ControllerInput {hUplus, hUminus, wUplus, wUminus, hDplus, hDminus, wDplus, wDminus, submit, noInput};

public class SceneManager : MonoBehaviour {

    public SerialHandler serialHandler;

    public static bool isChange = false;
    public static int devNum = 0;

    public static int p1 = 0;
    public static int p2 = 0;
    public static int p3 = 0;
    public static int devID = 0;

    int[][] shapeList = new int[][]
    {
        new int[] { 30, 30, 0, 0},
        new int[] { 180, 160, 70, 1},
        new int[] { 160, 160, 160, 2},
        new int[] { 180, 180, 120, 3},
        new int[] { 180, 180, 180, 4}
    };

    void Start () {
        serialHandler.OnDataReceived += SerialHandler_OnDataReceived;
        StartCoroutine("Playing");
        ChangeShape(shapeList[devNum]);
    }

    void Update()
    {

    }

    IEnumerator Playing()
    {
        while (true)
        {
            if (isChange)
            {
                isChange = false;
                ChangeShape(shapeList[devNum]);

            }
            yield return null;
        }

        yield break;
    }

    private void SerialHandler_OnDataReceived(string message)
    {
        Debug.Log(message);
        if (message == "moveFin")
        {
            serialHandler.Write("g\n");
        }
        var data = message.Split(
                new string[] { "\t" }, System.StringSplitOptions.None);
        if (data.Length < 2) return;
        
        try
        {
            //Debug.Log(message);
            //if (message == "moveFin") isPlaying = true;
        }
        catch (System.Exception e)
        {
            Debug.LogWarning(e.Message);
        }
    }

    private void ChangeShape(int[] shape)
    {
        p1 = shape[0];
        p2 = shape[1];
        p3 = shape[2];
        devID = shape[3];
        Debug.Log(string.Format("Change to {0}, {1}, {2}, {3}", p1, p2, p3, devID));
        string a = string.Format("a{0}\n", p1);
        string b = string.Format("b{0}\n", p2);
        string c = string.Format("c{0}\n", p3);
        serialHandler.Write(a);
        serialHandler.Write(b);
        serialHandler.Write(c);
    }

    private void ChangeShapeToInitial()
    {
        ChangeShape(new int[4] { 0, 0, 0, 0 });
    }

    private void OnApplicationQuit()
    {
        ChangeShapeToInitial();
    }
}
