using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class animatorTest : MonoBehaviour {

    Animator animator;
    float HP = 40;
    public static bool isAttacked = false;
    public GameObject EnergyField;

	// Use this for initialization
	void Start () {
        animator = GetComponent<Animator>();
        StartCoroutine("Appear");
	}
	
	// Update is called once per frame
	void Update () {
	}

    IEnumerator Appear()
    {
        EnergyField.SetActive(true);
        while (transform.position.y < 0)
        {
            transform.position = transform.position + new Vector3(0, 0.01f, 0);
            yield return new WaitForSeconds(0.01f);
        }
        SetTrigger("isAppeared");
        StartCoroutine("Normal");
    }

    IEnumerator Normal()
    {
        while (!animator.GetCurrentAnimatorStateInfo(0).IsTag("Normal"))
        {
            yield return null;
        }
        changeWeapon.changeTime = 3f;
        changeWeapon.isChangeWeapon = true;
        while (HP > 20)
        {
            if (Input.GetKeyDown(KeyCode.A) || isAttacked 
                && animator.GetCurrentAnimatorStateInfo(0).IsTag("Normal"))
            {
                SetTrigger("isGetHitTrigger");
                HP -= 10;
                isAttacked = false;
            }
            yield return null;
        }
        while (true)
        {
            if (Input.GetKeyDown(KeyCode.A) || isAttacked 
                && animator.GetCurrentAnimatorStateInfo(0).IsTag("Normal"))
            {
                GetAngry();
                isAttacked = false;
                break;
            }
            yield return null;
        }
        yield return new WaitForSeconds(1f);
        StartCoroutine("Angry");
    }

    IEnumerator Angry()
    {
        changeWeapon.changeTime = 3f;
        changeWeapon.isChangeWeapon = true;
        while (HP > 0)
        {
            if (Input.GetKeyDown(KeyCode.A) || isAttacked 
                && animator.GetCurrentAnimatorStateInfo(0).IsTag("Angry"))
            {
                SetTrigger("isGetHitTrigger");
                HP -= 10;
                isAttacked = false;
            }
            yield return null;
        }
        while (true)
        {
            if(Input.GetKeyDown(KeyCode.A) || isAttacked 
                && animator.GetCurrentAnimatorStateInfo(0).IsTag("Angry"))
            {
                Dead();
                isAttacked = false;
                break;
            }
            yield return null;
        }
    }


    void GetAngry()
    {
        SetTrigger("isGetAngryTrigger");
    }

    void Dead()
    {
        SetTrigger("isDeathTrigger");
        Destroy(EnergyField);
    }

    void SetBool(string boolName, bool state)
    {
        animator.SetBool(boolName, state);
    }

    void SetTrigger(string triggerName)
    {
        animator.SetTrigger(triggerName);
    }
}
