using System.Diagnostics;

namespace Files
{
    public partial class Form : System.Windows.Forms.Form
    {
        OpenFileDialog ofd;
        List<string> listWords;
        public Form()
        {
            InitializeComponent();
            ofd = new();
            listWords = [];
            ChooseFile.Click += GetWords;
            SearchButton.Click += Search;
        }
        private void GetWords(object? sender, EventArgs e)
        {
            ofd.Filter = "(*.txt)|*.txt";
            ofd.ShowDialog();
            Stopwatch sw = new();
            sw.Start();
            string[] words = File.ReadAllText(ofd.FileName).Split();
            for (int i = 0; i < words.Length; i++) if (!listWords.Contains(words[i])) listWords.Add(words[i]);
            sw.Stop();
            Time1.Text = sw.Elapsed.ToString();
        }
        private void Search(object? sender, EventArgs e)
        {
            listBox.Items.Clear();
            Stopwatch sw = new();
            sw.Start();
            string word = SearchBox.Text;
            foreach (string s in listWords)
            {
                if (s.Contains(word)) listBox.Items.Add(s);
            }
            sw.Stop();
            Time2.Text = sw.Elapsed.ToString();
        }
    }
}
