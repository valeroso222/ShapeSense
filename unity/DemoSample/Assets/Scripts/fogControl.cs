using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class fogControl : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetKeyDown(KeyCode.A))
        {
            Example();
        }
	}

    void Example()
    {
        // Set the fog color to be blue
        RenderSettings.fogDensity *= 0.9f;

        // And enable fog
        //RenderSettings.fog = true;
    }
}
