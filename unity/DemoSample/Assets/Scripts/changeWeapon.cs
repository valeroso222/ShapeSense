using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class changeWeapon : MonoBehaviour {

    public GameObject effects;
    public GameObject nextWeapon;
    public int nextWeaponNum;
    public static bool isChangeWeapon = false;
    public static float changeTime = 3f;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetKeyDown(KeyCode.C) || isChangeWeapon)
        {
            isChangeWeapon = false;
            SceneManager.devNum = nextWeaponNum;
            SceneManager.isChange = true;
            Instantiate(effects, transform.parent);
            StartCoroutine("Change");
        }
	}

    IEnumerator Change()
    {
        yield return new WaitForSeconds(changeTime);
        nextWeapon.SetActive(true);
        gameObject.SetActive(false);
    }
}
