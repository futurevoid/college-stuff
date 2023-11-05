namespace CS102_Section2
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.studgrd = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.submitbtn = new System.Windows.Forms.Button();
            this.exitbtn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // studgrd
            // 
            this.studgrd.AutoSize = true;
            this.studgrd.Font = new System.Drawing.Font("Segoe UI Semibold", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.studgrd.Location = new System.Drawing.Point(25, 25);
            this.studgrd.Name = "studgrd";
            this.studgrd.Size = new System.Drawing.Size(126, 21);
            this.studgrd.TabIndex = 0;
            this.studgrd.Text = "Student\'s Grade";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(25, 228);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(484, 23);
            this.textBox1.TabIndex = 1;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // submitbtn
            // 
            this.submitbtn.Location = new System.Drawing.Point(437, 54);
            this.submitbtn.Name = "submitbtn";
            this.submitbtn.Size = new System.Drawing.Size(96, 33);
            this.submitbtn.TabIndex = 2;
            this.submitbtn.Text = "Submit";
            this.submitbtn.UseVisualStyleBackColor = true;
            this.submitbtn.Click += new System.EventHandler(this.button1_Click);
            // 
            // exitbtn
            // 
            this.exitbtn.Location = new System.Drawing.Point(437, 112);
            this.exitbtn.Name = "exitbtn";
            this.exitbtn.Size = new System.Drawing.Size(96, 35);
            this.exitbtn.TabIndex = 3;
            this.exitbtn.Text = "Exit";
            this.exitbtn.UseVisualStyleBackColor = true;
            this.exitbtn.Click += new System.EventHandler(this.button2_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(545, 263);
            this.Controls.Add(this.exitbtn);
            this.Controls.Add(this.submitbtn);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.studgrd);
            this.Name = "Form1";
            this.Text = "Grading Portal";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Label studgrd;
        private TextBox textBox1;
        private Button submitbtn;
        private Button exitbtn;
    }
}