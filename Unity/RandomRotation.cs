using UnityEngine;

public class RandomRotation : MonoBehaviour
{
    // Variables pour la vitesse de rotation minimale et maximale, configurables depuis l'inspector
    [SerializeField] private float minRotationSpeed = 10f;
    [SerializeField] private float maxRotationSpeed = 100f;

    // Variable priv�e pour stocker la vitesse de rotation actuelle
    private float rotationSpeed;

    // Variable priv�e pour stocker l'axe de rotation al�atoire
    private Vector3 randomRotationAxis;

    void Start()
    {
        // Choisir une vitesse de rotation al�atoire entre minRotationSpeed et maxRotationSpeed
        rotationSpeed = Random.Range(minRotationSpeed, maxRotationSpeed);

        // G�n�rer un axe de rotation al�atoire
        randomRotationAxis = Random.onUnitSphere;
    }

    void Update()
    {
        // Appliquer la rotation au cube autour de l'axe de rotation al�atoire
        transform.Rotate(randomRotationAxis, rotationSpeed * Time.deltaTime);
    }
}
