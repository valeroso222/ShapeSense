using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class samehadaNormal : MonoBehaviour
{

    //Rigidbody rb;
    Vector3 lastXaxis;
    float xDot;
    float xAngle;
    Vector3 lastTopPos;
    float topDistance;
    float d = 0.5f;
    Vector3 speed;

    public windGo windPrefab;

    // Use this for initialization
    void Start()
    {
        lastXaxis = transform.right;
        xAngle = Vector3.Angle(transform.right, lastXaxis);

        lastTopPos = transform.position + transform.up * d;
        StartCoroutine("calcDot");
    }

    // Update is called once per frame
    void Update()
    {
        RenderSettings.fogDensity += (0f - RenderSettings.fogDensity) * 0.01f;


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

            if (topDistance > 0.5 && xAngle < 10)
            {
                Debug.Log("Wielding");
                Emit();
                ClearFog();
            }

            lastXaxis = transform.right;

            lastTopPos = transform.position + transform.up * d;

            yield return new WaitForSeconds(0.05f);
        }
    }

    void Emit()
    {
        windGo windObject = (windGo)Instantiate(windPrefab, transform.position, Quaternion.identity);
        windObject.forward = transform.up;
        windObject.speed = topDistance * 20;
        
    }

    void ClearFog()
    {
        RenderSettings.fogDensity *= 0.7f;

    }

    private void OnTriggerEnter(Collider other)
    {
        Debug.Log("trigger enter");
        animatorTest.isAttacked = true;
    }

}
