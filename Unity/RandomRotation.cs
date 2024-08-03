using UnityEngine;

public class RandomRotation : MonoBehaviour
{
    // Variables pour la vitesse de rotation minimale et maximale, configurables depuis l'inspector
    [SerializeField] private float minRotationSpeed = 10f;
    [SerializeField] private float maxRotationSpeed = 100f;

    // Variable privée pour stocker la vitesse de rotation actuelle
    private float rotationSpeed;

    // Variable privée pour stocker l'axe de rotation aléatoire
    private Vector3 randomRotationAxis;

    void Start()
    {
        // Choisir une vitesse de rotation aléatoire entre minRotationSpeed et maxRotationSpeed
        rotationSpeed = Random.Range(minRotationSpeed, maxRotationSpeed);

        // Générer un axe de rotation aléatoire
        randomRotationAxis = Random.onUnitSphere;
    }

    void Update()
    {
        // Appliquer la rotation au cube autour de l'axe de rotation aléatoire
        transform.Rotate(randomRotationAxis, rotationSpeed * Time.deltaTime);
    }
}
