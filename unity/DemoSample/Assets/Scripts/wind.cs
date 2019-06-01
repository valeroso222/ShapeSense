using UnityEngine;
using System.Collections;

public class wind : MonoBehaviour
{
    public float coefficient;   // 空気抵抗係数
    public Vector3 velocity;    // 風速

    void OnTriggerStay(Collider col)
    {

        Debug.Log("hit");
        if (col.GetComponent<Rigidbody>() == null)
        {
            return;
        }
        Debug.Log("hit");

        // 相対速度計算
        var relativeVelocity = velocity - col.GetComponent<Rigidbody>().velocity;

        // 空気抵抗を与える
        col.GetComponent<Rigidbody>().AddForce(coefficient * relativeVelocity);
    }
}