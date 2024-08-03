using UnityEngine;

public class RandomShapeGenerator : MonoBehaviour
{
    public int shapeCount = 10; // Nombre de formes à générer
    public float shapeSize = 1.0f; // Taille des formes
    public Vector3[] customPositions; // Positions spécifiques pour les formes

    //private GameObject previousShape;

    // Référence au SynthWorkingPlayer
    public SynthWorkingPlayer synthWorkingPlayer;

    void Start()
    {
       
        for (int i = 0; i < shapeCount; i++)
        {
            GenerateRandomShape(i);
        }
    }

    void GenerateRandomShape(int index)
    {
        if (customPositions == null || customPositions.Length == 0)
        {
            Debug.LogError("Aucune position spécifique n'a été définie.");
            return;
        }
        
        // Sélectionner une position spécifique à partir du tableau
        Vector3 randomPosition = customPositions[index % customPositions.Length];

        // Générer une forme aléatoire
        GameObject shape = null;
        int shapeType = Random.Range(0, 2);
        switch (shapeType)
        {
            case 0:
                shape = CreateCube();
                break;
            case 1:
                shape = CreateSphere();
                break;
            case 2:
                shape = CreateCylinder();
                break;
                /*  case 3:
                      shape = CreateCone();
                      break;
                  case 4:
                      shape = CreatePyramid();
                      break;
                  case 5:
                      shape = CreateTorus();
                      break;
                */
        }

        // Générer une couleur aléatoire
        Renderer renderer = shape.GetComponent<Renderer>();
        renderer.material.color = new Color(Random.value, Random.value, Random.value);

        // Positionner et redimensionner la forme
        shape.transform.position = randomPosition;
        shape.transform.localScale = Vector3.one * shapeSize;

        // Ajouter une rotation aléatoire
        shape.transform.rotation = Random.rotation;

        // Ajouter un script pour faire tourner la forme de manière aléatoire
        shape.AddComponent<RandomRotation>();
       // previousShape = shape;

        // Notifier le SynthWorkingPlayer de la forme générée
        if (synthWorkingPlayer != null)
        {
            synthWorkingPlayer.targetGameObject = shape;
        }
    }

   /* public void DestroyPreviousShape()
    {
        // Détruire la forme précédente s'il y en a une
      /*  if (previousShape != null)
        {
            Destroy(previousShape);
        }
        GameObject cubeObject = GameObject.Find("Cube");
        if (cubeObject != null)
        {
            Destroy(cubeObject);
        }
        GameObject sphereObject = GameObject.Find("Sphere");
        if (sphereObject != null)
        {
            Destroy(sphereObject);
        }
        GameObject torusObject = GameObject.Find("Torus");
        if (torusObject != null)
        {
            Destroy(torusObject);
        }
        GameObject cylinderObject = GameObject.Find("Cylinder");
        if (cylinderObject != null)
        {
            Destroy(cylinderObject);
        }
    }*/


    GameObject CreateCube()
    {

        GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
        cube.tag = "GeneratedShape";
        return cube;
    }

    GameObject CreateSphere()
    {
        GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        sphere.tag = "GeneratedShape";
        return sphere;
    }

    GameObject CreateCylinder()
    {
        GameObject cylinder = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
        cylinder.tag = "GeneratedShape";
        return cylinder;
    }

    GameObject CreateTorus()
    {
        GameObject torus = new GameObject("Torus");
        torus.tag = "GeneratedShape";
        MeshFilter meshFilter = torus.AddComponent<MeshFilter>();
        MeshRenderer meshRenderer = torus.AddComponent<MeshRenderer>();

        Mesh mesh = new Mesh();

        int segments = 24;
        int tubeSegments = 16;
        float radius = 1f;
        float tubeRadius = 0.3f;

        Vector3[] vertices = new Vector3[segments * tubeSegments];
        int[] triangles = new int[segments * tubeSegments * 6];

        for (int i = 0; i < segments; i++)
        {
            float theta = 2 * Mathf.PI * i / segments;
            Vector3 center = new Vector3(Mathf.Cos(theta) * radius, 0, Mathf.Sin(theta) * radius);

            for (int j = 0; j < tubeSegments; j++)
            {
                float phi = 2 * Mathf.PI * j / tubeSegments;
                Vector3 normal = new Vector3(Mathf.Cos(phi) * Mathf.Cos(theta), Mathf.Sin(phi), Mathf.Cos(phi) * Mathf.Sin(theta));
                vertices[i * tubeSegments + j] = center + normal * tubeRadius;
            }
        }

        int index = 0;
        for (int i = 0; i < segments; i++)
        {
            for (int j = 0; j < tubeSegments; j++)
            {
                int nextI = (i + 1) % segments;
                int nextJ = (j + 1) % tubeSegments;

                triangles[index++] = i * tubeSegments + j;
                triangles[index++] = nextI * tubeSegments + j;
                triangles[index++] = i * tubeSegments + nextJ;

                triangles[index++] = nextI * tubeSegments + j;
                triangles[index++] = nextI * tubeSegments + nextJ;
                triangles[index++] = i * tubeSegments + nextJ;
            }
        }

        mesh.vertices = vertices;
        mesh.triangles = triangles;
        mesh.RecalculateNormals();

        meshFilter.mesh = mesh;
        return torus;
    }
    GameObject CreateCone()
    {
        GameObject cone = new GameObject("Cone");
        cone.tag = "GeneratedShape";
        MeshFilter meshFilter = cone.AddComponent<MeshFilter>();
        MeshRenderer meshRenderer = cone.AddComponent<MeshRenderer>();

        Mesh mesh = new Mesh();

        int segments = 24;
        float radius = 1f;
        float height = 2f;

        Vector3[] vertices = new Vector3[segments + 2];
        int[] triangles = new int[segments * 3 * 2];

        vertices[0] = Vector3.up * height;
        for (int i = 0; i < segments; i++)
        {
            float angle = 2 * Mathf.PI * i / segments;
            float x = radius * Mathf.Cos(angle);
            float z = radius * Mathf.Sin(angle);
            vertices[i + 1] = new Vector3(x, 0, z);
        }
        vertices[segments + 1] = Vector3.zero;

        int index = 0;
        for (int i = 0; i < segments; i++)
        {
            triangles[index++] = 0;
            triangles[index++] = i + 1;
            triangles[index++] = (i + 1) % segments + 1;

            triangles[index++] = segments + 1;
            triangles[index++] = (i + 1) % segments + 1;
            triangles[index++] = i + 1;
        }

        mesh.vertices = vertices;
        mesh.triangles = triangles;
        mesh.RecalculateNormals();

        meshFilter.mesh = mesh;
        return cone;
    }
    GameObject CreatePyramid()
    {
        GameObject pyramid = new GameObject("Pyramid");
        pyramid.tag = "GeneratedShape";
        MeshFilter meshFilter = pyramid.AddComponent<MeshFilter>();
        MeshRenderer meshRenderer = pyramid.AddComponent<MeshRenderer>();

        Mesh mesh = new Mesh();

        Vector3[] vertices = new Vector3[]
        {
            new Vector3(0, 1, 0), new Vector3(-1, -1, -1), new Vector3(1, -1, -1),
            new Vector3(1, -1, 1), new Vector3(-1, -1, 1)
        };

        int[] triangles = new int[]
        {
            0, 1, 2,
            0, 2, 3,
            0, 3, 4,
            0, 4, 1,
            1, 3, 2,
            1, 4, 3
        };

        mesh.vertices = vertices;
        mesh.triangles = triangles;
        mesh.RecalculateNormals();

        meshFilter.mesh = mesh;
        return pyramid;
    }
}
