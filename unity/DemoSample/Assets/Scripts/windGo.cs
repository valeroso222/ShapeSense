using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class windGo : MonoBehaviour {

    public float speed;
    public Vector3 forward;
    float time = 0;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        float sp = speed * Time.deltaTime;
        transform.position = new Vector3(transform.position.x + sp*forward.x, transform.position.y + sp*forward.y, transform.position.z + sp*forward.z);
        time += Time.deltaTime;
        if (time > 5) Destroy(gameObject);
    }
}
