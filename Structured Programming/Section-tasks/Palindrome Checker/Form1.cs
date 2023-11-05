namespace Palindrome_Checker
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            var input = textBox1.Text;
            var rev = "";
           if (input != null)
            {
                for (int i = input.Length - 1; i >= 0; i--)
                {
                    rev += input[i].ToString();
                }
                if (rev == input)
                {
                    label1.Text = $"String is Palindrome {input} == {rev}";
                }
                else
                {
                    label1.Text = $"String is not Palindrome {input} != {rev}";
                }
            }
            
            if (input == "")
            {
                label1.Text = "result";

            }
        }

    }
}