using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class shuriken : MonoBehaviour {

    Rigidbody rb;
    public GameObject player;

	// Use this for initialization
	void Start () {
        rb = GetComponent<Rigidbody>();
        rb.angularVelocity = transform.up*(-1000);
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetKeyDown(KeyCode.B))
        {
            Vector3 direction = (player.transform.position - transform.position)*10 + transform.up*5;
            rb.AddForce(direction);
            rb.useGravity = true;
        }
	}
}
