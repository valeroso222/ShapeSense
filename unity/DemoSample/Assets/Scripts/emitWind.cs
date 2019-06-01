using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class emitWind : MonoBehaviour {

    //public GameObject windPrefab;
    public windGo windPrefab;
	// Use this for initialization
	void Start () {
        //StartCoroutine("Emit");
	}

    // Update is called once per frame
    void Update()
    {
        
    }

    IEnumerator Emit() {
        while (true)
        {
            windGo windObject = (windGo)Instantiate(windPrefab, transform.position,Quaternion.identity);
            windObject.forward = transform.up;
            yield return new WaitForSeconds(1);
        }
    }
}
