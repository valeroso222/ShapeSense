using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class madara : MonoBehaviour {

    //Rigidbody rb;
    Vector3 lastXaxis;
    float xDot;
    float xAngle;
    Vector3 lastTopPos;
    float topDistance;
    float d = 0.5f;
    Vector3 speed;
    public Animator animator;
    float fogMax = 1f;

    public windGo windPrefab;
    public GameObject Dragon;

    // Use this for initialization
    void Start () {
        lastXaxis = transform.right;
        xAngle = Vector3.Angle(transform.right, lastXaxis);

        lastTopPos = transform.position + transform.up * d;
        StartCoroutine("calcDot");
    }
	
	// Update is called once per frame
	void Update () {
        RenderSettings.fogDensity += (fogMax - RenderSettings.fogDensity) * 0.1f * Time.deltaTime;
        if (fogMax < 0.3 && fogMax > 0)
        {
            fogMax -= 0.1f * Time.deltaTime;
            Dragon.SetActive(true);
        }
    }

    IEnumerator calcDot()
    {
        while (true)
        {
            xDot = Vector3.Dot(transform.right, lastXaxis);
            xAngle = Vector3.Angle(transform.right, lastXaxis);
            topDistance = Vector3.Distance(lastTopPos, transform.position + transform.up * d);

            //Debug.Log(xDot);
            //Debug.Log(xAngle);
            //Debug.Log(topDistance.ToString("f1"));
            //Debug.Log(lastTopPos);

            if (topDistance > 0.2 && xAngle<10)
            {
                //Debug.Log("Wielding");
                Emit();
                clearFog();
            }

            lastXaxis = transform.right;

            lastTopPos = transform.position + transform.up * d;

            yield return new WaitForSeconds(0.02f);
        }
    }

    void Emit()
    {
        windGo windObject = (windGo)Instantiate(windPrefab, transform.position, Quaternion.identity);
        windObject.forward = transform.up;
        windObject.speed = topDistance*20;
    }

    void clearFog()
    {
        RenderSettings.fogDensity *= 0.7f;
        fogMax *= 0.95f;
        if (fogMax < 0.1) fogMax = 0.1f;
        
    }
}
