using UnityEngine;
using AK.Wwise;
using System.IO;
using UnityEditor;

public class SynthWorkingPresetCSV2 : MonoBehaviour
{
    [Range(-96f, 0f)]
    public float sliderRtpcVolume;
    [Range(0f, 100f)]
    public float sliderRtpcHighPass;
    [Range(0f, 100f)]
    public float sliderRtpcLowPass;
    [Range(-3600f, 3600f)]
    public float sliderRtpcPitch;
    [Range(-3600f, 3600f)]
    public float sliderRtpcTranspose;
    [Range(0f, 100f)]
    public float sliderRtpcSpeedPlay;
    [Range(-1f, 1f)]
    public float sliderRtpcAttackCurve;
    [Range(-1f, 1f)]
    public float sliderRtpcAttackTime;
    [Range(-1f, 1f)]
    public float sliderRtpcDecayTime;
    [Range(0f, 100f)]
    public float sliderRtpcLFODepth;
    [Range(0f, 20000f)]
    public float sliderRtpcLFOFrequency;

    public AK.Wwise.RTPC rtpcVolume;
    public AK.Wwise.RTPC rtpcHighPass;
    public AK.Wwise.RTPC rtpcLowPass;
    public AK.Wwise.RTPC rtpcPitch;
    public AK.Wwise.RTPC rtpcTranspose;
    public AK.Wwise.RTPC rtpcSpeedPlay;
    public AK.Wwise.RTPC rtpcAttackCurve;
    public AK.Wwise.RTPC rtpcAttackTime;
    public AK.Wwise.RTPC rtpcDecayTime;
    public AK.Wwise.RTPC rtpcLFODepth;
    public AK.Wwise.RTPC rtpcLFOFrequency;

    private void Awake()
    {
        LoadSliderValues2();
    }

    private void OnApplicationQuit()
    {
        SaveSliderValues2();
    }

    private void Update()
    {
        UpdateRTPCValues2();
    }

    private void UpdateRTPCValues2()
    {
        rtpcVolume.SetGlobalValue(sliderRtpcVolume);
        rtpcHighPass.SetGlobalValue(sliderRtpcHighPass);
        rtpcLowPass.SetGlobalValue(sliderRtpcLowPass);
        rtpcPitch.SetGlobalValue(sliderRtpcPitch);
        rtpcTranspose.SetGlobalValue(sliderRtpcTranspose);
        rtpcSpeedPlay.SetGlobalValue(sliderRtpcSpeedPlay);
        rtpcAttackCurve.SetGlobalValue(sliderRtpcAttackCurve);
        rtpcAttackTime.SetGlobalValue(sliderRtpcAttackTime);
        rtpcDecayTime.SetGlobalValue(sliderRtpcDecayTime);
        rtpcLFODepth.SetGlobalValue(sliderRtpcLFODepth);
        rtpcLFOFrequency.SetGlobalValue(sliderRtpcLFOFrequency);
    }

    private void SaveSliderValues2()
    {
        string path = Path.Combine(Application.persistentDataPath, "sliderValues2.txt");
        using (StreamWriter writer = new StreamWriter(path))
        {
            writer.WriteLine(sliderRtpcVolume);
            writer.WriteLine(sliderRtpcHighPass);
            writer.WriteLine(sliderRtpcLowPass);
            writer.WriteLine(sliderRtpcPitch);
            writer.WriteLine(sliderRtpcTranspose);
            writer.WriteLine(sliderRtpcSpeedPlay);
            writer.WriteLine(sliderRtpcAttackCurve);
            writer.WriteLine(sliderRtpcAttackTime);
            writer.WriteLine(sliderRtpcDecayTime);
            writer.WriteLine(sliderRtpcLFODepth);
            writer.WriteLine(sliderRtpcLFOFrequency);
        }
    }

    private void LoadSliderValues2()
    {
        string path = Path.Combine(Application.persistentDataPath, "sliderValues2.txt");
        if (File.Exists(path))
        {
            using (StreamReader reader = new StreamReader(path))
            {
                sliderRtpcVolume = float.Parse(reader.ReadLine());
                sliderRtpcHighPass = float.Parse(reader.ReadLine());
                sliderRtpcLowPass = float.Parse(reader.ReadLine());
                sliderRtpcPitch = float.Parse(reader.ReadLine());
                sliderRtpcTranspose = float.Parse(reader.ReadLine());
                sliderRtpcSpeedPlay = float.Parse(reader.ReadLine());
                sliderRtpcAttackCurve = float.Parse(reader.ReadLine());
                sliderRtpcAttackTime = float.Parse(reader.ReadLine());
                sliderRtpcDecayTime = float.Parse(reader.ReadLine());
                sliderRtpcLFODepth = float.Parse(reader.ReadLine());
                sliderRtpcLFOFrequency = float.Parse(reader.ReadLine());
            }
        }
    }

#if UNITY_EDITOR
    [CustomEditor(typeof(SynthWorkingPresetCSV2))]
    public class SynthWorkingPresetCSVEditor2 : Editor
    {
        public override void OnInspectorGUI()
        {
            DrawDefaultInspector();
            SynthWorkingPresetCSV2 script = (SynthWorkingPresetCSV2)target;
            if (GUILayout.Button("Save Preset to CSV"))
            {
                SavePresetToCSV(script);
            }
        }

        private string FormatFloat(float value)
        {
            return value.ToString("F6").Replace(',', '.');
        }

        private void SavePresetToCSV(SynthWorkingPresetCSV2 script)
        {
            string path = EditorUtility.SaveFilePanel("Save Preset", "", "preset.csv", "csv");
            if (string.IsNullOrEmpty(path)) return;

            using (StreamWriter writer = new StreamWriter(path))
            {
                writer.WriteLine("Volume" + "," + script.rtpcVolume + "," + FormatFloat(script.rtpcVolume.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
                writer.WriteLine("HighPass" + "," + script.rtpcHighPass + "," + FormatFloat(script.rtpcHighPass.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
                writer.WriteLine("LowPass" + "," + script.rtpcLowPass + "," + FormatFloat(script.rtpcLowPass.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
                writer.WriteLine("Pitch " + "," + script.rtpcPitch + "," + FormatFloat(script.rtpcPitch.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
                writer.WriteLine("Transpose " + "," + script.rtpcTranspose + "," + FormatFloat(script.rtpcTranspose.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
                writer.WriteLine("SpeedPlay " + "," + script.rtpcSpeedPlay + "," + FormatFloat(script.rtpcSpeedPlay.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
                writer.WriteLine("AttackCurve " + "," + script.rtpcAttackCurve + "," + FormatFloat(script.rtpcAttackCurve.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
                writer.WriteLine("AttackTime" + "," + script.rtpcAttackTime + "," + FormatFloat(script.rtpcAttackTime.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
                writer.WriteLine("DecayTime" + "," + script.rtpcDecayTime + "," + FormatFloat(script.rtpcDecayTime.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
                writer.WriteLine("LFODepth" + "," + script.rtpcLFODepth + "," + FormatFloat(script.rtpcLFODepth.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
                writer.WriteLine("LFOFrequency" + "," + script.rtpcLFOFrequency + "," + FormatFloat(script.rtpcLFOFrequency.GetValue(script.gameObject)) + "," + "0.0" + "," + "0.0");
            }

            Debug.Log("Preset saved to " + path);
            AssetDatabase.Refresh();
        }
    }
#endif
}
