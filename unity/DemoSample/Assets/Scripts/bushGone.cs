using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bushGone : MonoBehaviour {

    Rigidbody rb;

	// Use this for initialization
	void Start () {
        rb = GetComponent<Rigidbody>();
        rb.AddForce(new Vector3(0, 100, 100));
    }
	
	// Update is called once per frame
	void Update () {
	}
}
